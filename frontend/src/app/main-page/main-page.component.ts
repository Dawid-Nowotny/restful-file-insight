import { Component } from '@angular/core';
import { ServerService } from '../server.service';
import { HttpErrorResponse } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { Validators, FormBuilder, FormsModule, ReactiveFormsModule } from '@angular/forms';
import { UploadFileData } from '../models/upload-file-data.model';

@Component({
  selector: 'app-main-page',
  standalone: true,
  imports: [CommonModule, FormsModule, ReactiveFormsModule],
  templateUrl: './main-page.component.html',
  styleUrl: './main-page.component.scss'
})
export class MainPageComponent {
  loading: boolean;
  fileName: string;
  form: any;
  uploadFileData: UploadFileData;
  success: boolean;
  errorMessage: string;
  response: any;

  constructor(private formBuilder: FormBuilder, private serverService: ServerService) {
    this.loading = false;
    this.fileName = "";
    this.uploadFileData = new UploadFileData();
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
    })
  }

  get f() {
      return this.form.controls;
  }

  uploadFile(event: any) {
      this.uploadFileData.file = event.target.files[0];
  }

  onSubmit() {
    if (!this.uploadFileData.file) {
      this.errorMessage = "Nie wybrano pliku!";
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
    formData.append("file", this.uploadFileData.file);
    this.fileName = this.uploadFileData.file.name;

    this.serverService.uploadFileMagicNumbers(formData).subscribe(
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