import { Routes } from '@angular/router';
import { MainPageComponent } from './main-page/main-page.component';
import { NotFoundComponent } from './not-found/not-found.component';

export const routes: Routes = [
    { path: '', component: MainPageComponent },
    { path: 'main', component: MainPageComponent },
    { path: '**', pathMatch: 'full', 
        component: NotFoundComponent },
  ];