import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VaccinesSummaryTableComponent } from './vaccines-summary-table.component';

describe('VaccinesSummaryTableComponent', () => {
  let component: VaccinesSummaryTableComponent;
  let fixture: ComponentFixture<VaccinesSummaryTableComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ VaccinesSummaryTableComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(VaccinesSummaryTableComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
