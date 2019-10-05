import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute, ParamMap } from '@angular/router';
import { DataService } from '@services/data.service';
import { map } from 'rxjs/operators';

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
    this.getStock(ticker);
  }

  private getStock(ticker: string) {
    this.dataService.get(ticker).subscribe(
      data => { this.stockData = data; },
      err => console.error(err),
      () => { console.log(this.stockData) }
    );
  }
}
