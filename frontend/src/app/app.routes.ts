import { Routes } from '@angular/router';
import { MainPageComponent } from './main-page/main-page.component';
import { ScanComponent } from './scan/scan.component';
import { NotFoundComponent } from './not-found/not-found.component';

export const routes: Routes = [
    { path: '', component: MainPageComponent },
    { path: 'scan', component: ScanComponent },
    { path: 'compare', component: MainPageComponent },
    { path: '**', pathMatch: 'full', 
        component: NotFoundComponent },
  ];