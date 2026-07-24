# Day 13 – Linux Volume Management (LVM)

### Task 1: Check Current Storage
Run: `lsblk`, `pvs`, `vgs`, `lvs`, `df -h`


**Observation** : 
- Three disk/EBS volume is attached to the server.
- All three volume's are not mounted anywhere.
- No PV, GV & LV are avilable.

  ![Task1](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-13/Images/Task1.jpg)

### Task 2: Create Physical Volume
```bash
pvcreate /dev/nvme1n1 /dev/nvme2n1  
pvs
```
**Observation** : Two physical Volume of size 6G & 8G is created.

![Task2](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-13/Images/Task2.jpg)



### Task 3: Create Volume Group
```bash
vgcreate devops-vg /dev/sdb
vgs
```

**Observation** : Volume group of size 14G is created from two physical volume.

![Task3](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-13/Images/Task3.png)

### Task 4: Create Logical Volume
```bash
lvcreate -L 10G -n app-data devops-vg
lvs
```
**Observation** : Logical Volume of 10G is created.

![Task4](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-13/Images/task4.png)

### Task 5: Format and Mount
```bash
mkfs.ext4 /dev/devops-vg/app-data
mkdir -p /mnt/app-data
mount /dev/devops-vg/app-data /mnt/app-data
df -h /mnt/app-data
```
**Observation** :
- ext4 file system created.
- mounted the logical volume.

![Task5](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-13/Images/Task5.jpg)

### Task 6: Extend the Volume
```bash
lvextend -L +200M /dev/devops-vg/app-data
resize2fs /dev/devops-vg/app-data
df -h /mnt/app-data
```

![Task6](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-13/Images/Task6.jpg)

