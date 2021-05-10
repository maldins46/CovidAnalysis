import { TestBed } from '@angular/core/testing';

import { CookieAcceptanceService } from './cookie-acceptance.service';

describe('CookieAcceptationService', () => {
  let service: CookieAcceptanceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(CookieAcceptanceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
