import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

const httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable({
    providedIn: 'root'
})

export class ServerService {
    private restUrl = 'http://127.0.0.1:8000';
    constructor(private http: HttpClient) { }

    uploadFileMagicNumbers(file: any): Observable<any> {
        const url = `${this.restUrl}/file/check-magic-numbers`;
        return this.http.post(url, file);
    }

    uploadFileScan(file: any): Observable<any> {
        const url = `${this.restUrl}/file/scan`;
        return this.http.post(url, file);
    }
    uploadCompare(file: any): Observable<any> {
        const url = `${this.restUrl}/file/compare_files`;
        return this.http.post(url, file);
    }
}
