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
    this.getStocks();
  }

  // Adding this to a separate method, instead of just adding this whole block
  // into ngOnInit(), because I want to be able to call this at other times
  // besides on init. For example, if a stock is added, this could potentially
  // be a way  to reload all stocks.

  public getStocks() {
    this.dataService.getAllStocks().subscribe(
      data => {
        this.stocks = data['Stocks'];
        // NOTE: This seems backwards; we should be setting this.stocks from
        //       dataService.stocks, but I don't want to call the database
        //       twice. With this setup, the data goes:
        //           component -> service -> db -> component -> service
        //       Ideally, I want the data to go:
        //          component -> service -> db -> *service* -> *component*
        this.dataService.stocks = this.stocks;
      },
      err => console.error(err),
      () => {
        this.itemsToShow = this.stocks.slice(0, this.initialItemsShowed);
      }
    );
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
