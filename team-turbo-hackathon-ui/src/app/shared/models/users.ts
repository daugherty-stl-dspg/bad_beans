export interface Users {
  firstName: string;
  lastName: string;
  user_id: string;
  email: string;
  los: string;
  photo: File;
  status: string;
  _id: {
    $oid: string;
  };
  lastUpdated: string;
}
