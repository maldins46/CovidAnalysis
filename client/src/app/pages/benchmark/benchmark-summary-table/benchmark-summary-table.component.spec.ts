import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BenchmarkSummaryTableComponent } from './benchmark-summary-table.component';

describe('BenchmarkSummaryTableComponent', () => {
  let component: BenchmarkSummaryTableComponent;
  let fixture: ComponentFixture<BenchmarkSummaryTableComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ BenchmarkSummaryTableComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(BenchmarkSummaryTableComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
