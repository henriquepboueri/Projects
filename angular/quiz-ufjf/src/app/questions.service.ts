import { Injectable } from '@angular/core';
import { Question } from './models/question.model';

@Injectable({
  providedIn: 'root',
})
export class QuestionsService {
  questions: Question[] = [
    {
      id: 1,
      text:
        'O campus avançado da UFJF iniciou suas atividades em GV no ano de 2012.  Qual o mês de início dos trabalhos?',
      options: [
        { id: 1, text: 'Março' },
        { id: 2, text: 'Junho' },
        { id: 3, text: 'Novembro' },
      ],
      answerIndex: 3,
    },
    {
      id: 2,
      text:
        'Em outubro de 2016 a UFJF GV realizou a primeira colação de grau do campus avançado. Qual curso celebrou este importante momento?',
      options: [
        { id: 1, text: 'Ciências Econômicas' },
        { id: 2, text: 'Educação Física' },
        { id: 3, text: 'Administração' },
      ],
      answerIndex: 1,
    },
    {
      id: 3,
      text:
        'Antes da chegada da Covid-19, todos os calouros podiam participar da Gincana Solidária, um importante momento de integração e de ajuda humanitária. Até agosto de 2019 qual o número de alimentos arrecadados pelo projeto?',
      options: [
        { id: 1, text: '7 toneladas' },
        { id: 2, text: '9 toneladas' },
        { id: 3, text: '11 toneladas' },
      ],
      answerIndex: 2,
    },
    {
      id: 4,
      text:
        'Um grande potencial da UFJF GV é sua articulação com a comunidade, com destaque para os projetos de Extensão. Em abril de 2021 a UFJF tinha 39 projetos. Quantos eram de GV?',
      options: [
        { id: 1, text: '17' },
        { id: 2, text: '20' },
        { id: 3, text: '23' },
      ],
      answerIndex: 2,
    },
    {
      id: 5,
      text:
        'O empenho da equipe da UFJF garantiu que a universidade conquistasse cinco programas de pós-graduação antes de completar 10 anos de existência. O primeiro programa chegou em 2016. Você sabe qual é?',
      options: [
        { id: 1, text: 'PMBqBM' },
        { id: 2, text: 'Ciências Aplicadas à Saúde' },
        { id: 3, text: 'PROFBIO' },
      ],
      answerIndex: 1,
    },
    {
      id: 6,
      text:
        'Além de excelente corpo técnico, a UFJF GV conta com diferentes espaços para que os estudantes coloquem em prática seu conhecimento. Entre esses espaços está a Clínica-Escola de Fisioterapia, inaugurada em 2016. Qual a média de atendimentos mensais na clínica?',
      options: [
        { id: 1, text: '350' },
        { id: 2, text: '500' },
        { id: 3, text: '700' },
      ],
      answerIndex: 3,
    },
    {
      id: 7,
      text:
        'Entre 2016 e 2018, a UFJF GV manteve o projeto Coral Universitário, que chegou a reunir mais de 50 coralistas. Quantas apresentações o Coral fez durante esses 3 anos?',
      options: [
        { id: 1, text: '3 apresentações' },
        { id: 2, text: '6 apresentações' },
        { id: 3, text: '9 apresentações' },
      ],
      answerIndex: 3,
    },
    {
      id: 8,
      text:
        'Todos os estudantes da UFJF GV contam com importante apoio do setor de Apoio Estudantil, que integram atendimentos nas áreas de Pedagogia, Psicologia e Serviço Social. Em que mês e ano o setor foi implantado?',
      options: [
        { id: 1, text: 'agosto de 2014' },
        { id: 2, text: 'outubro de 2015' },
        { id: 3, text: 'março de 2017' },
      ],
      answerIndex: 1,
    },
    {
      id: 9,
      text:
        'A Pesquisa dentro das instituições de ensino é muito importante para o desenvolvimento da ciência. Seis cursos da UFJF GV já formalizaram grupos de pesquisa. Quantos grupos de pesquisa o campus avançado já tem?',
      options: [
        { id: 1, text: '8 grupos' },
        { id: 2, text: '10 grupos' },
        { id: 3, text: '12 grupos' },
      ],
      answerIndex: 2,
    },
    {
      id: 10,
      text:
        'Assim como o campus de Juiz de Fora, GV realiza anualmente a Semana de Ciência, Tecnologia e Sociedade, um importante evento que integra ensino, pesquisa, extensão e inovação. Em 2019 o campus avançado realizou qual edição do evento?',
      options: [
        { id: 1, text: '4ª edição' },
        { id: 2, text: '5ª edição' },
        { id: 3, text: '6ª edição' },
      ],
      answerIndex: 1,
    },
  ];

  constructor() {}

  getQuestions() {
    return this.questions.slice();
  }
}