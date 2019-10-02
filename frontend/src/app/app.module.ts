// Angular
import { HttpClientModule } from '@angular/common/http';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

// Services
import { DataService } from '@app/services/data.service';

// Modules
import { SharedModule } from '@shared/shared.module';

// Components
import { AllStocksComponent } from './stocks/all-stocks/all-stocks.component';

@NgModule({
  declarations: [ AppComponent, AllStocksComponent ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    SharedModule,
    HttpClientModule
  ],
  providers: [ DataService ],
  bootstrap: [ AppComponent ]
})

export class AppModule { }
