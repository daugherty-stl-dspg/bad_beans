import { Component, OnInit, Inject } from '@angular/core';
import { MatDialog, MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { DialogData } from 'src/app/shared/models/dialogData';
import { FormGroup, FormBuilder, ReactiveFormsModule, FormControl, NgControl } from '@angular/forms';
import { UserWithPhoto } from 'src/app/shared/models/userWithPhoto';

@Component({
  selector: 'app-view-details',
  templateUrl: './view-details.component.html',
  styleUrls: ['./view-details.component.scss']
})
export class ViewDetailsComponent {

  userWithPhotos: UserWithPhoto[] = [];

  public name = '';
  newForm: FormGroup;

  constructor(
    public dialogRef: MatDialogRef<ViewDetailsComponent>,
    private fb: FormBuilder
  ) {
    this.createForm();
  }

  onNoClick(): void {
    this.dialogRef.close();
  }

  updateName(value) {
    this.dialogRef.close(value);
  }

  createForm() {
    this.newForm = this.fb.group({
      firstName: [''],
      lastName: ['']
    });
  }


}
