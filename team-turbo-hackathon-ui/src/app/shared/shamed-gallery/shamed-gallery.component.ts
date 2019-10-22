import { UserService } from './../services/user.service';
import { Component, OnInit } from '@angular/core';
import { Users } from '../models/users';
import { UserWithPhoto } from '../models/userWithPhoto';

@Component({
  selector: 'app-shamed-gallery',
  templateUrl: './shamed-gallery.component.html',
  styleUrls: ['./shamed-gallery.component.scss']
})
export class ShamedGalleryComponent implements OnInit {

  shamedUsers: Users[];
  userWithPhotos: UserWithPhoto[] = [];

  constructor(
    private userService: UserService
  ) { }

  ngOnInit() {
    this.userService.getAllUsers().subscribe(result => {
      this.shamedUsers = result.filter(s => s.status === '0');
      this.shamedUsers.map(user => {
        this.userService.addPhotosToUser(user.user_id).subscribe(photo => {
          let currentPhoto = photo
          this.userWithPhotos.push(new UserWithPhoto(
            user.user_id,
            photo,
            this.convertHexToTime(user._id.$oid),
            user.firstName,
            user.lastName,
            user.los,
            user.lastUpdated
          ));
          this.userWithPhotos.sort();
        });
      });
    });
  }

  convertHexToTime(objectId) {
    return parseInt(objectId.substring(0, 8), 16);
  }

}
