import { Component } from '@angular/core';
import { ServerService } from '../server.service';
import { HttpErrorResponse } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { UploadFileData } from '../models/upload-file-data.model';
import { Validators, FormBuilder, FormsModule, ReactiveFormsModule } from '@angular/forms';

@Component({
  selector: 'app-compare',
  standalone: true,
  imports: [CommonModule, FormsModule, ReactiveFormsModule],
  templateUrl: './compare.component.html',
  styleUrl: './compare.component.scss'
})
export class CompareComponent {
  loading: boolean;
  fileName: string;
  file2Name: string;
  form: any;
  uploadFileData: UploadFileData;
  uploadFile2Data: UploadFileData;
  success: boolean;
  errorMessage: string;
  response: any;

  constructor(private formBuilder: FormBuilder, private serverService: ServerService) {
    this.loading = false;
    this.fileName = "";
    this.file2Name = "";
    this.uploadFileData = new UploadFileData();
    this.uploadFile2Data = new UploadFileData();
    this.success = false;
    this.errorMessage = '';
    this.response = '';
  }

  ngOnInit() {
    this.creatForm();
  }

  creatForm() {
    this.form = this.formBuilder.group({
        file: [null, Validators.required],
        file2: [null, Validators.required],
    })
  }

  get f() {
      return this.form.controls;
  }

  uploadFile(event: any, file1: boolean) {
    if(file1)
      this.uploadFileData.file = event.target.files[0];
    else
      this.uploadFile2Data.file = event.target.files[0];
  }


  onSubmit() {
    if (!this.uploadFileData.file && !this.uploadFile2Data.file) {
      this.errorMessage = "Nie wybrano plików!";
      this.success = false;
      return;
    }

    this.loading = true;
    this.success = true;
    this.errorMessage = "";

    if (this.form.invalid) {
        return
    }

    const formData = new FormData();
    formData.append("file1", this.uploadFileData.file);
    formData.append("file2", this.uploadFile2Data.file);
    this.fileName = this.uploadFileData.file.name;
    this.file2Name = this.uploadFile2Data.file.name;

    this.serverService.uploadCompare(formData).subscribe(
        {
            next: (response: any) => {
                this.response = response;
                this.success = true;
                this.loading = false;
            },
            error: (error: HttpErrorResponse) => {
                if (error.status === 0) {
                    this.errorMessage = "Wystąpił błąd po stronie serwera.";
                } else {
                    this.errorMessage = error.error.detail;
                }
                this.success = false;
                this.loading = false;
            }
        }
    )
  }
}