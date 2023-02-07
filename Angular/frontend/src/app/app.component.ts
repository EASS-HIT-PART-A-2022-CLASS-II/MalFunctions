import { HttpClient } from '@angular/common/http';
import { Component, ViewChild } from '@angular/core';
import { DxDataGridComponent } from 'devextreme-angular';
import notify from 'devextreme/ui/notify';
import { flatMap, map } from 'rxjs/operators';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {


  @ViewChild('gridContainer', { static: false }) dataGrid!: DxDataGridComponent;

  constructor(private http: HttpClient) { }

  title = 'MalFunction';

  statusTypes = [
    { id: 1, status: "Pending", color: "#bee0ec" },
    { id: 2, status: "In Progress", color: "orange" },
    { id: 3, status: "Completed", color: "#aee5a8" },
  ]

  newMalList: any = [];
  completed: any = []

  ngOnInit() {
    this.http.get("http://localhost:8083/check").subscribe(res => {
      //console.log("result from check:", res);
      if (res == "exists" || res == "created") {
        notify("Database approved, ready for work", 'success', 3000);
      }
      this.getData();
    }, err => {
      notify("Error, cannot approve database", 'error', 3000);
    });
  }

  insertRow(e: any) {
    e.data.status = 1;
    e.data.date = Date.now();
  }

  onRowInserted(e: any) {
    console.log("Date(new): ", e.data.date);
    let obj = {
      id: 0,
      description: e.data.description,
      creator: e.data.creator,
      date: Number.isInteger(e.data.date) ? e.data.date : Date.parse(e.data.date),
      status: e.data.status
    };

    this.http.post("http://localhost:8083/addMal", obj).subscribe(res => {
      //console.log("backFrom sql: ", res);
      if (res == "Added") {
        notify("Malfunction added", 'success', 3000);
        this.getData();
      }
    }, err => {
      notify("Error, Failed to add Malfunction", 'error', 3000);
    });
  }
  onRowRemoved(e: any) {
    this.http.delete("http://localhost:8083/delMal/" + e.data.id).subscribe(res => {
      if (res == "Removed") {
        this.dataGrid.instance.refresh()
        notify("Malfunction was removed", 'success', 3000);
      }
    }, err => {
      notify("Error, cannot remove Malfunction", 'error', 3000);
    })
  }


  RowUpdated(e: any) {
    console.log("Date(update): ", e.data.date);
    let obj = {
      id: e.data.id,
      description: e.data.description,
      creator: e.data.creator,
      date: Number.isInteger(e.data.date) ? e.data.date : Date.parse(e.data.date),
      status: e.data.status
    };

    //console.log("Sent after edit: ", obj);
    this.http.post("http://localhost:8083/editMal", obj).subscribe(res => {
      if (res == "Edited") {
        notify("Malfunction was edited", 'success', 3000);
        this.getData();
      }
    }, err => {
      notify("Error, cannot edit Malfunction", 'error', 3000);
    });


  }
  onRowPrepared(e: any) {
    if (e.rowType === "data") {
      let obj = this.statusTypes.find((obj: any) => obj.id === e.data.status);
      e.rowElement.bgColor = obj?.color; //set the background color based on the data
    }
    if (e.rowType === "header") {
      e.rowElement.bgColor = "#cacbca"; //set the background color based on the data
    }

  }
  //orgTables(e: any) {
  //  let obj = this.newMalList.find((obj: any) => obj.id === e.data.id);
  //  this.completed.push(obj);
  //  this.newMalList = this.newMalList.filter((item: any) => item.id !== e.data.id);
  //}
  getData() {
    this.http.get("http://localhost:8083/getList").subscribe((res: any) => {
      //console.log("Result: ", res);
      this.newMalList = [];
      this.completed = [];
      res.forEach((data: any) => {
        //console.log("data: ", data)
        if (data.status == 3) {
          this.completed.push(data)
        }
        else {
          this.newMalList.push(data)
        }
      });

    }, err => {
      notify("Error, cannot get malfunction list", 'error', 3000);
    });
  }

}
