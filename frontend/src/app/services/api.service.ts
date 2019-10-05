/*
  ApiService:
    This service will basically be an abstract generic class to contact the API.
*/

import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private prefix = 'http://localhost:8080/stocks/api/v1.0';
  constructor(private http: HttpClient) {}

  private formatErrors(error: any) { return throwError(error.error); }

  public get(path: string, params: HttpParams = new HttpParams()): Observable<any> {
    return this.http.get(`${ this.prefix }${ path }`, { params })
      .pipe(catchError(this.formatErrors));
  }
}
