export class UserWithPhoto {
  user_id: string;
  photo: string;
  $oid: number;
  firstName: string;
  lastName: string;
  los: string;
  lastUpdated: string;

  constructor(
    user_id: string,
    photo: string,
    $oid: number,
    firstName: string,
    lastName: string,
    los: string,
    lastUpdated: string
  ) {
    this.user_id = user_id;
    this.photo = photo;
    this.$oid = $oid;
    this.firstName = firstName;
    this.lastName = lastName;
    this.los = los;
    this.lastUpdated = lastUpdated;
  }
}
