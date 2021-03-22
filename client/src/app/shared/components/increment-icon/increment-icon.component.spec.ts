import { ComponentFixture, TestBed } from '@angular/core/testing';

import { IncrementIconComponent } from './increment-icon.component';

describe('IncrementIconComponent', () => {
  let component: IncrementIconComponent;
  let fixture: ComponentFixture<IncrementIconComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ IncrementIconComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(IncrementIconComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
