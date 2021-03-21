import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MarcheSummaryTableComponent } from './marche-summary-table.component';

describe('MarcheSummaryTableComponent', () => {
  let component: MarcheSummaryTableComponent;
  let fixture: ComponentFixture<MarcheSummaryTableComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MarcheSummaryTableComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(MarcheSummaryTableComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
