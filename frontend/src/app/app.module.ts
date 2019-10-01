import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { SharedModule } from '@shared/shared.module';
import { AllStocksComponent } from './stocks/all-stocks/all-stocks.component';

@NgModule({
  declarations: [ AppComponent, AllStocksComponent, ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    SharedModule
  ],
  providers: [],
  bootstrap: [ AppComponent ]
})

export class AppModule { }
