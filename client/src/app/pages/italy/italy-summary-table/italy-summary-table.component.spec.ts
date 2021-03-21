import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ItalySummaryTableComponent } from './italy-summary-table.component';

describe('ItalySummaryTableComponent', () => {
  let component: ItalySummaryTableComponent;
  let fixture: ComponentFixture<ItalySummaryTableComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ItalySummaryTableComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ItalySummaryTableComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
