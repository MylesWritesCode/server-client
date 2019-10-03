import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class DataService {
  prefix = 'http://localhost:8080/stocks/api/v1.0';
  api:string;

  constructor(private http: HttpClient) { }

  getAllStocks() {
    return this.http.get(this.prefix + '/allStocks');
  }
}
