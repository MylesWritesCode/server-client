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
    if (!this.stocks) {
      this.getStocks();
    }
  }

  // Adding this to a separate method, instead of just adding this whole block
  // into ngOnInit(), because I want to be able to call this at other times
  // besides on init. For example, if a stock is added, this could potentially
  // be a way  to reload all stocks.
  getStocks() {
    // NOTE: Stocks is the hardcoded return from the API. There's probably a
    //       better way to do this dynamically, but I know that I sent one
    //       large JSON package with the key 'Stocks' and value of more objects.

    // NOTE: (update) Rather than having the stocks loaded in the data service,
    //       I'm going to load it here when the user loads the all stocks
    //       component. One benefit is that we don't load all the data
    //       immediately, but it's a little slower when users load the all
    //       stocks component.
    this.dataService.getAllStocks().subscribe(
      data => { this.stocks = data['Stocks']; },
      err => console.error(err),
      () => {
        console.log("Stocks loaded!");
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
