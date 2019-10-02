import { Component, OnInit } from '@angular/core';
import { DataService } from '@app/services/data.service';

@Component({
  selector: 'app-all-stocks',
  templateUrl: './all-stocks.component.html',
  styleUrls: ['./all-stocks.component.scss']
})
export class AllStocksComponent implements OnInit {
  public stocks;

  constructor(private _dataService: DataService) { }

  ngOnInit() {
    this.getStocks();
  }

  // Adding this to a separate method, instead of just adding this whole block
  // into ngOnInit(), because I want to be able to call this at other times
  // besides on init. For example, if a stock is added, this could potentially
  // be a way  to reload all stocks.
  getStocks() {
    this._dataService.getAllStocks().subscribe(
      data => { this.stocks = data },
      err => console.error(err),
      () => console.log('Finished loading stocks...')
    );
  }
}
