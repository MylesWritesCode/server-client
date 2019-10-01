import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

import { FooterComponent } from '@shared/footer/footer.component';
import { HeaderComponent } from '@shared/header/header.component';
import { SidebarComponent } from '@shared/sidebar/sidebar.component';

@NgModule({
  declarations: [ HeaderComponent, FooterComponent, SidebarComponent ],
  imports: [ CommonModule, RouterModule ],
  exports: [ HeaderComponent, FooterComponent, SidebarComponent ]
})

export class SharedModule { }
