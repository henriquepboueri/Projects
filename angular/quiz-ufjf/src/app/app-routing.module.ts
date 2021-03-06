import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { HomeComponent } from './home/home.component';
import { InstrucoesComponent } from './instrucoes/instrucoes.component';
import { QuizComponent } from './quiz/quiz.component';
import { RankingComponent } from './ranking/ranking.component';
import { ResultadoComponent } from './resultado/resultado.component';

const routes: Routes = [
  { path: '', component: HomeComponent, pathMatch: 'full' },
  { path: 'quiz', component: QuizComponent },
  { path: 'instrucoes', component: InstrucoesComponent },
  { path: 'ranking', component: RankingComponent },
  { path: 'resultado', component: ResultadoComponent, data: { message: '' } },
  { path: '**', component: HomeComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
