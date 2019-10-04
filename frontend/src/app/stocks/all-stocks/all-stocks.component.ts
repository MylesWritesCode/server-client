import { Component, OnInit } from '@angular/core';
import { DataService } from '@app/services/data.service';

@Component({
  selector: 'app-all-stocks',
  templateUrl: './all-stocks.component.html',
  styleUrls: ['./all-stocks.component.scss']
})
export class AllStocksComponent implements OnInit {
  private initialItemsShowed: number = 10;
  private itemsToLoad: number = 10;

  public stocks;
  public selectedStock: string;
  public itemsToShow: any;
  public isFullListDisplayed: boolean = false;


  constructor(private dataService: DataService) { }

  ngOnInit() {
    // if (!this.stocks) {
    //   this.getStocks();
    // }
    console.log('trying to get stocks from service');
    this.getStocks();
    console.log('finished trying to get stocks');
    console.log(this.stocks);
  }

  // Adding this to a separate method, instead of just adding this whole block
  // into ngOnInit(), because I want to be able to call this at other times
  // besides on init. For example, if a stock is added, this could potentially
  // be a way  to reload all stocks.
  public getStocks() {
    this.stocks = this.dataService.getAllStocks();
  }

  show(index) {
    this.selectedStock = index;
  }

  // Called when the window is scrolled down via infinite-scroll package. It
  // basically paginates the loading of all stocks, so that we don't front load
  // all the data on the inital load.
  onScroll() {
    if (this.initialItemsShowed <= this.stocks.length) {
      this.initialItemsShowed += this.itemsToLoad;
      this.itemsToShow = this.stocks.slice(0, this.initialItemsShowed);
    } else {
      this.isFullListDisplayed = true;
    }
  }
}
