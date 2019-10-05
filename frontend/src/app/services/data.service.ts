/*
  DataService:
    This service simply uses ApiService to contact the API with respect to
    stocks.
  NOTE:
    I should probably rename this service to StockService, since it only deals
    with stocks now, but I'll leave it for now.
*/

import { ApiService } from '@services/api.service';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DataService {
  private prefix = 'http://localhost:8080/stocks/api/v1.0';
  private api: string;

  // public stocks: object[];
  public selectedStock: string;

  constructor(private apiService: ApiService) { }

  // NOTE: Stocks is the hardcoded return from the API. There's probably a
  //       better way to do this dynamically, but I know that I sent one
  //       large JSON package with the key 'Stocks' and value of more objects.

  // public getAllStocksz(): Observable<any> {
  //   return this.http.get(this.prefix + '/allStocks').pipe();
  // }

  public getAllStocks(): Observable<any> {
    return this.apiService.get('/allStocks');
  }

  public get(slug): Observable<any> {
    this.selectedStock = slug;
    return this.apiService.get('/getStock/' + slug);
  }
}
