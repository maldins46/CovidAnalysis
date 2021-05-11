import {ComponentFixture, TestBed, waitForAsync} from '@angular/core/testing';

import { NestedAppbarComponent } from './nested-appbar.component';

describe('NestedAppbarComponent', () => {
  let component: NestedAppbarComponent;
  let fixture: ComponentFixture<NestedAppbarComponent>;

  beforeEach(waitForAsync(() => {
    TestBed.configureTestingModule({
      declarations: [ NestedAppbarComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(NestedAppbarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
