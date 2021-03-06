// Angular
import { HttpClientModule } from '@angular/common/http';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

// Services
import { DataService } from '@services/data.service';

// Modules
import { SharedModule } from '@shared/shared.module';
import { InfiniteScrollModule } from 'ngx-infinite-scroll';

// Components
import { AllStocksComponent } from './stocks/all-stocks/all-stocks.component';
import { StockComponent } from './stocks/stock/stock.component';

@NgModule({
  declarations: [ AppComponent, AllStocksComponent, StockComponent ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    SharedModule,
    HttpClientModule,
    InfiniteScrollModule
  ],
  providers: [ DataService ],
  bootstrap: [ AppComponent ]
})

export class AppModule { }
