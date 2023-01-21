
import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { DxButtonModule, DxDataGridModule } from 'devextreme-angular';



import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    DxButtonModule,
    BrowserModule,
    HttpClientModule,
    DxDataGridModule,
    
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
