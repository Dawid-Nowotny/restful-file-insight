import { Component } from '@angular/core';
import { ServerService } from '../server.service';
import { HttpErrorResponse } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { Validators, FormBuilder, FormsModule, ReactiveFormsModule } from '@angular/forms';
import { UploadImageData } from '../models/upload-image-data.model';

@Component({
  selector: 'app-main-page',
  standalone: true,
  imports: [CommonModule, FormsModule, ReactiveFormsModule],
  templateUrl: './main-page.component.html',
  styleUrl: './main-page.component.scss'
})
export class MainPageComponent {
  submitted: boolean;
  submitDisabled: boolean;
  form: any;
  uploadImageData: UploadImageData;
  successMessage: string;
  errorMessage: string;

  constructor(private formBuilder: FormBuilder, private serverService: ServerService) {
    this.submitted = false;
    this.submitDisabled = false;
    this.uploadImageData = new UploadImageData();
    this.successMessage = '';
    this.errorMessage = '';
  }

  ngOnInit() {
    this.creatForm();
  }

  creatForm() {
    this.form = this.formBuilder.group({
        image: [null, Validators.required],
    })
  }

  get f() {
      return this.form.controls;
  }

  uploadImage(event: any) {
      this.uploadImageData.file = event.target.files[0];
  }

  onSubmit() {
    this.submitted = true;
    this.successMessage = "";
    this.errorMessage = "";

    if (this.form.invalid) {
        return
    }

    this.submitDisabled = true;

    const formData = new FormData();
    formData.append("file", this.uploadImageData.file);

    this.serverService.uploadImageMagicNumbers(formData).subscribe(
        {
            next: (response: any) => {
                this.successMessage = "Zdjęcie zostało dodane!";
                this.submitted = false;
                this.submitDisabled = false;
            },
            error: (error: HttpErrorResponse) => {
                if (error.status === 0) {
                    this.errorMessage = "Wystąpił błąd po stronie serwera.";
                } else {
                    this.errorMessage = error.error.detail;
                }

                this.submitted = false;
                this.submitDisabled = false;
            }
        }
    )
  }
}
