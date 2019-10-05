import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute, ParamMap } from '@angular/router';
import { DataService } from '@services/data.service';

@Component({
  selector: 'app-stock',
  templateUrl: './stock.component.html',
  styleUrls: ['./stock.component.scss']
})
export class StockComponent implements OnInit {
  private stockData;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private dataService: DataService
  ) {}

  ngOnInit() {
    let ticker = this.route.snapshot.paramMap.get('ticker');
    console.log(ticker);
    this.getStock(ticker);

    console.log(this.stockData);
  }

  private getStock(ticker: string) {
    this.dataService.get(ticker).subscribe(
      data => { this.stockData = data; },
      err => console.error(err),
      () => {}
    );
  }
}
