import {
  Component,
  EventEmitter,
  Input,
  OnInit,
  Output,
  ViewChild,
} from '@angular/core';
import { MatRadioGroup } from '@angular/material/radio';

import { Question } from '../models/question.model';

@Component({
  selector: 'app-question',
  templateUrl: './question.component.html',
  styleUrls: ['./question.component.css'],
})
export class QuestionComponent implements OnInit {
  @Input() question: Question;
  @Output() chosenOption = new EventEmitter<{
    questionId: number;
    answerId: number;
  }>();
  @ViewChild(MatRadioGroup) radioGroup: MatRadioGroup;

  constructor() {}

  ngOnInit(): void {}

  onSelectOption(optionId) {
    this.chosenOption.emit({
      questionId: this.question.id,
      answerId: optionId.id,
    });
  }
}