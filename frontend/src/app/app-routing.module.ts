import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { AllStocksComponent } from '@app/stocks/all-stocks/all-stocks.component';
import { StockComponent } from '@app/stocks/stock/stock.component';

const routes: Routes = [
  { path: 'all-stocks', component: AllStocksComponent },
  { path: 'stocks/:ticker', component: StockComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
