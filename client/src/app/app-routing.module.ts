import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {HomeComponent} from './pages/home/home.component';
import {ConnectionGuard, OnlineGuard} from './core/guards/connection.guard';
import {OfflineComponent} from './pages/offline/offline.component';
import {PageNotFoundComponent} from './pages/page-not-found/page-not-found.component';
import {ItalyComponent} from './pages/italy/italy.component';
import {MarcheComponent} from './pages/marche/marche.component';
import {VaccinesComponent} from './pages/vaccines/vaccines.component';
import {FeedComponent} from './pages/feed/feed.component';

const routes: Routes = [
  { path: '', redirectTo: 'home', pathMatch: 'full' },
  { path: 'home', component: HomeComponent, canActivate: [ConnectionGuard] },
  { path: 'italy', component: ItalyComponent, canActivate: [ConnectionGuard] },
  { path: 'vaccines', component: VaccinesComponent, canActivate: [ConnectionGuard] },
  { path: 'marche', component: MarcheComponent, canActivate: [ConnectionGuard] },
  { path: 'feed', component: FeedComponent, canActivate: [ConnectionGuard] },

  // others
  { path: 'offline', component: OfflineComponent, canActivate: [OnlineGuard] },
  { path: '404', component: PageNotFoundComponent },
  { path: '**', redirectTo: '404' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes, {scrollPositionRestoration: 'enabled'})],
  exports: [RouterModule]
})
export class AppRoutingModule { }
