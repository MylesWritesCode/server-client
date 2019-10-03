import { Component, OnInit, Input } from '@angular/core';
import { DataService } from '@app/services/data.service';

@Component({
  selector: 'app-all-stocks',
  templateUrl: './all-stocks.component.html',
  styleUrls: ['./all-stocks.component.scss']
})
export class AllStocksComponent implements OnInit {
  private initialItemsShowed: number = 5;
  private itemsToLoad: number = 5;

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

  onScroll() {
    if (this.initialItemsShowed <= this.stocks.length) {
      this.initialItemsShowed += this.itemsToLoad;
      this.itemsToShow = this.stocks.slice(0, this.initialItemsShowed);
    } else {
      this.isFullListDisplayed = true;
    }
  }
}
