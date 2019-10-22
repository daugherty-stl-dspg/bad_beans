import { Component, OnInit } from '@angular/core';
import { UserService } from '../services/user.service';
import { Users } from '../models/users';

@Component({
  selector: 'app-full-gallery',
  templateUrl: './full-gallery.component.html',
  styleUrls: ['./full-gallery.component.scss']
})
export class FullGalleryComponent implements OnInit {

  famedUsers: Users[];
  fakePhoto: string;

  constructor(
    private userService: UserService
  ) { }

  ngOnInit() {
    this.userService.getAllUsers().subscribe(result => {
      this.famedUsers = result.filter(s => s.status === '1');
    });
  }

  getFakePhoto() {
    this.userService.getFakePhotos().subscribe(result => {
      this.fakePhoto = result
    });
  }

}
