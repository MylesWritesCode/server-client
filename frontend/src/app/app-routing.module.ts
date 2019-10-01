import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AppComponent } from './app.component';
import { AllStocksComponent } from './stocks/all-stocks/all-stocks.component';

const routes: Routes = [
  { path: 'all-stocks', component: AllStocksComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
