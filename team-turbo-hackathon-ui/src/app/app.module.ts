import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MatButtonModule, MatCheckboxModule, MatSidenavModule, MatTabsModule, MatToolbarModule, MatIconModule, MatListModule, MatMenuModule, MatFormFieldModule, MatInputModule, MatDialog, MatDialogModule, MAT_DIALOG_DEFAULT_OPTIONS, MatDialogClose, MatDialogConfig } from '@angular/material';
import { HeaderComponent } from './shared/components/navigation/header/header.component';
import { LayoutComponent } from './shared/components/layout/layout.component';
import { SidenavListComponent } from './shared/components/navigation/sidenav-list/sidenav-list.component';
import { MostRecentRowComponent } from './shared/components/most-recent-row/most-recent-row.component';
import { MatCardModule } from '@angular/material/card';
import { DashboardComponent } from './dashboard/dashboard.component';
import { FullGalleryComponent } from './shared/full-gallery/full-gallery.component';
import { HallOfFameComponent } from './hall-of-fame/hall-of-fame.component';
import { HallOfShameComponent } from './hall-of-shame/hall-of-shame.component';
import { LoginComponent } from './login/login.component';
import { ViewDetailsComponent } from './shared/components/modal/view-details/view-details.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { LogoutComponent } from './shared/components/logout/logout.component';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { RecentFameRowComponent } from './shared/components/recent-fame-row/recent-fame-row.component';
import { ShamedGalleryComponent } from './shared/shamed-gallery/shamed-gallery.component';


@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    LayoutComponent,
    SidenavListComponent,
    MostRecentRowComponent,
    DashboardComponent,
    FullGalleryComponent,
    HallOfFameComponent,
    HallOfShameComponent,
    LoginComponent,
    ViewDetailsComponent,
    LogoutComponent,
    RecentFameRowComponent,
    ShamedGalleryComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatButtonModule,
    MatCheckboxModule,
    MatSidenavModule,
    MatToolbarModule,
    MatIconModule,
    MatListModule,
    MatMenuModule,
    MatCardModule,
    MatFormFieldModule,
    MatInputModule,
    MatDialogModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule
  ],
  providers: [
    { provide: MAT_DIALOG_DEFAULT_OPTIONS, useValue: { hasBackdrop: true } },
    MatDialog,
    MatDialogConfig,
    HttpClient
  ],
  exports: [
    MatTabsModule,
    MatSidenavModule,
    MatToolbarModule,
    MatIconModule,
    MatButtonModule,
    MatListModule,
    MatMenuModule,
    MostRecentRowComponent,
    MatFormFieldModule,
    MatInputModule
  ],
  entryComponents: [
    ViewDetailsComponent
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
