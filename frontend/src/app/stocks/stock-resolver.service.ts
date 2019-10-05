import { Injectable } from '@angular/core';
import { ActivatedRouteSnapshot, Resolve, Router, RouterStateSnapshot } from '@angular/router';
import { Observable } from 'rxjs';

import { DataService } from '@services/data.service';

@Injectable()
export class StockResolver implements Resolve<any> {
  constructor(
    private dataService: DataService,
    private router: Router
  ) {}
}

