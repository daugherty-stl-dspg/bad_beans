import { FullGalleryComponent } from './shared/full-gallery/full-gallery.component';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HallOfShameComponent } from './hall-of-shame/hall-of-shame.component';
import { HallOfFameComponent } from './hall-of-fame/hall-of-fame.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { LoginComponent } from './login/login.component';
import { LogoutComponent } from './shared/components/logout/logout.component';
import { ShamedGalleryComponent } from './shared/shamed-gallery/shamed-gallery.component';

const routes: Routes = [
  { path: 'home', component: DashboardComponent },
  { path: 'shame', component: ShamedGalleryComponent },
  { path: 'fame', component: FullGalleryComponent },
  { path: 'login', component: LoginComponent },
  { path: 'logout', component: LogoutComponent },
  { path: '', redirectTo: '/home', pathMatch: 'full' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
  declarations: []
})
export class AppRoutingModule { }
