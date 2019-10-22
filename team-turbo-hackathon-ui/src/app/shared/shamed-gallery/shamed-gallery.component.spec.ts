import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ShamedGalleryComponent } from './shamed-gallery.component';

describe('ShamedGalleryComponent', () => {
  let component: ShamedGalleryComponent;
  let fixture: ComponentFixture<ShamedGalleryComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ShamedGalleryComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ShamedGalleryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
