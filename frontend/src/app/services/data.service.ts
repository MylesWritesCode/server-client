import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map, observeOn } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class DataService {
  private prefix = 'http://localhost:8080/stocks/api/v1.0';
  private api: string;

  public stocks: object;

  constructor(private http: HttpClient) { }

  // NOTE: Stocks is the hardcoded return from the API. There's probably a
  //       better way to do this dynamically, but I know that I sent one
  //       large JSON package with the key 'Stocks' and value of more objects.

  public getAllStocks() {
    this.http.get(this.prefix + '/allStocks').subscribe(
      data => {
        this.stocks = data['Stocks'];
        console.log('stocks loaded into service');
      },
      err => console.error(err),
      () => {
        // console.log(this.stocks);
        return this.stocks;
      }
    );
  }
}
