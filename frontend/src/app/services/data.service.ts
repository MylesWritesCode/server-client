import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DataService {
  private prefix = 'http://localhost:8080/stocks/api/v1.0';
  private api: string;

  public stocks: object;
  public obs = new Observable();

  constructor(private http: HttpClient) { }

  // NOTE: Stocks is the hardcoded return from the API. There's probably a
  //       better way to do this dynamically, but I know that I sent one
  //       large JSON package with the key 'Stocks' and value of more objects.

  public getAllStocks(): any {
    this.http.get(this.prefix + '/allStocks').subscribe(
      data => {
        this.stocks = data['Stocks'];
        console.log('retrieved stocks and set in service');
        console.log(this.stocks);
      },
      err => console.error(err),
      // This is kinda cool, the following line will simply return this.stocks
      // to the caller.
      () => {
        console.log('got stocks...')
        return this.stocks;
      }
    );
  }
}
