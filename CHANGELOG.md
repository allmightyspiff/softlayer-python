# Change Log

## [6.1.3] - 2022-11-30

#### What's Changed
* New Command: Hardware notifications by @caberos in https://github.com/softlayer/softlayer-python/pull/1756
* New Command: virtual notifications by @caberos in https://github.com/softlayer/softlayer-python/pull/1758
* Change regex in rich text in simple option in help text by @edsonarios in https://github.com/softlayer/softlayer-python/pull/1759
* pip prod(deps): bump rich from 12.5.1 to 12.6.0 by @dependabot in https://github.com/softlayer/softlayer-python/pull/1760
* add more information to vs credentials by @caberos in https://github.com/softlayer/softlayer-python/pull/1762
* Fixed maxint issue by @allmightyspiff in https://github.com/softlayer/softlayer-python/pull/1765
* Added csv output format by @edsonarios in https://github.com/softlayer/softlayer-python/pull/1766
* add more information on hw credentials by @caberos in https://github.com/softlayer/softlayer-python/pull/1767
* Delete twitter link in documentation by @edsonarios in https://github.com/softlayer/softlayer-python/pull/1769
* new command hw create-credential by @caberos in https://github.com/softlayer/softlayer-python/pull/1774
* fix the hw credential error by @caberos in https://github.com/softlayer/softlayer-python/pull/1781
* Added test suite for py311 by @allmightyspiff in https://github.com/softlayer/softlayer-python/pull/1784
* New feature to change theme in slcli like dark, light o maintain in default by @edsonarios in https://github.com/softlayer/softlayer-python/pull/1775
* Match `virtual detail --prices` option with `hardware detail --prices` option by @BrianSantivanez in https://github.com/softlayer/softlayer-python/pull/1780
* Fixing preset-list pricing table by @allmightyspiff in https://github.com/softlayer/softlayer-python/pull/1782
* fix the call api cannot handle empty results by @caberos in https://github.com/softlayer/softlayer-python/pull/1789
* Debug output changed to a valid JSON by @edsonarios in https://github.com/softlayer/softlayer-python/pull/1791
* slcli hw add-notifications crashes with a bad user by @caberos in https://github.com/softlayer/softlayer-python/pull/1786
* del-notification commands, rename the commands to notifications-add by @caberos in https://github.com/softlayer/softlayer-python/pull/1785
* Add --extras to slcli order quote by @caberos in https://github.com/softlayer/softlayer-python/pull/1792
* An error is displaying for volume with replica in slcli for Active pr… by @caberos in https://github.com/softlayer/softlayer-python/pull/1794


**Full Changelog**: https://github.com/softlayer/softlayer-python/compare/v6.1.2...v6.1.3


## [6.1.2] - 2022-09-23

#### What's Changed
* Snapcraft: Updated to Core22 and  add homeishome-launch by @kz6fittycent in https://github.com/softlayer/softlayer-python/pull/1740
* Add status, create date and domain columns in `slcli vs list command` by @BrianSantivanez in https://github.com/softlayer/softlayer-python/pull/1728
* New command: ipsec cancel by @caberos in https://github.com/softlayer/softlayer-python/pull/1729
* New command: subnet clear-route by @caberos in https://github.com/softlayer/softlayer-python/pull/1738
* Deprecate slcli hw guests by @caberos in https://github.com/softlayer/softlayer-python/pull/1736
* Remove real usersnames from test fixtrues by @caberos in https://github.com/softlayer/softlayer-python/pull/1743
* Fix tox request.get hangout issue by @caberos in https://github.com/softlayer/softlayer-python/pull/1746
* add vs user-access command by @caberos in https://github.com/softlayer/softlayer-python/pull/1741
* Update Help message for commands that take in multiple arguments by @caberos in https://github.com/softlayer/softlayer-python/pull/1748
* Error with slcli order item-list by @caberos in https://github.com/softlayer/softlayer-python/pull/1751
* deprecate sl `autoscale` by @BrianSantivanez in https://github.com/softlayer/softlayer-python/pull/1753
* Unhandled error running a subcommand in slcli by @caberos in https://github.com/softlayer/softlayer-python/pull/1754


**Full Changelog**: https://github.com/softlayer/softlayer-python/compare/v6.1.1...v6.1.2


## [6.1.1] - 2022-08-18

#### What's Changed
* v6.1.0 Changelog and version bump by @allmightyspiff in https://github.com/softlayer/softlayer-python/pull/1674
* item-list fix by @allmightyspiff in https://github.com/softlayer/softlayer-python/pull/1679
* updating release job to actually publish to pypi by @allmightyspiff in https://github.com/softlayer/softlayer-python/pull/1680
* Update command - slcli object-storage endpoints by @edsonarios in https://github.com/softlayer/softlayer-python/pull/1685
* add the block volume-options command by @caberos in https://github.com/softlayer/softlayer-python/pull/1681
* add the file volume-options command by @caberos in https://github.com/softlayer/softlayer-python/pull/1684
* fixed issues where a message warned users about closing datacenter by @allmightyspiff in https://github.com/softlayer/softlayer-python/pull/1688
* Enable --format=raw and fixes table width  by @allmightyspiff in https://github.com/softlayer/softlayer-python/pull/1689
* Update `slcli hardware sensor` by @BrianSantivanez in https://github.com/softlayer/softlayer-python/pull/1691
* Improved successful response to command - slcli vs cancel by @edsonarios in https://github.com/softlayer/softlayer-python/pull/1695
* Fixed an issue with printing tables that contained empty items by @allmightyspiff in https://github.com/softlayer/softlayer-python/pull/1697
* Added a dependabot scanner  by @allmightyspiff in https://github.com/softlayer/softlayer-python/pull/1699
* block|file volume-options improvements by @caberos in https://github.com/softlayer/softlayer-python/pull/1700
* Option create-options in commands hardware and dedicatedhost fixed by @edsonarios in https://github.com/softlayer/softlayer-python/pull/1703
* pip prod(deps): bump rich from 12.3.0 to 12.5.1 by @dependabot in https://github.com/softlayer/softlayer-python/pull/1704
* block/file volume-options improvements 2 by @caberos in https://github.com/softlayer/softlayer-python/pull/1702
* New command ipsec order by @caberos in https://github.com/softlayer/softlayer-python/pull/1698
* block/file volume-options improvement 3 by @caberos in https://github.com/softlayer/softlayer-python/pull/1705
* Command slcli vlan create - displaying an error message by @edsonarios in https://github.com/softlayer/softlayer-python/pull/1707
* New Command: user device-access by @caberos in https://github.com/softlayer/softlayer-python/pull/1712
* Command slcli vlan edit accept that we do not send any parameters by @edsonarios in https://github.com/softlayer/softlayer-python/pull/1709
* Updated command - slcli vlan list by @edsonarios in https://github.com/softlayer/softlayer-python/pull/1713
* `slcli block subnets-list` command display an error message by @BrianSantivanez in https://github.com/softlayer/softlayer-python/pull/1716
* add user remove-access command by @caberos in https://github.com/softlayer/softlayer-python/pull/1717
* Add Devices with Trunks to vlan detail by @edsonarios in https://github.com/softlayer/softlayer-python/pull/1721
* slcli hardware reflash-firmware command does not display success message by @BrianSantivanez in https://github.com/softlayer/softlayer-python/pull/1724
* Fix bug with command - slcli cdn edit by @edsonarios in https://github.com/softlayer/softlayer-python/pull/1726

#### New Contributors
* @dependabot made their first contribution in https://github.com/softlayer/softlayer-python/pull/1704

**Full Changelog**: https://github.com/softlayer/softlayer-python/compare/v6.1.0...v6.1.1



## [6.1.0] - 2022-06-30

#### Major Updates
* [Rich](https://github.com/Textualize/rich) tables by @allmightyspiff in https://github.com/softlayer/softlayer-python/pull/1646
* [Rich](https://github.com/Textualize/rich) Text support by @allmightyspiff in https://github.com/softlayer/softlayer-python/pull/1635

Rich Text and Rich Tables will modernize the output of the SLCLI to be a little nicer to look at, with colors and other highlighting.

![image](https://user-images.githubusercontent.com/7408017/176753783-f6a4a43a-53ac-4600-a24f-21362f152747.png)
![image](https://user-images.githubusercontent.com/7408017/176753845-32af33f0-454f-4bab-ac63-1ae3db788ede.png)


#### What's Changed
* slcli licenses is missing the help text by @caberos in https://github.com/softlayer/softlayer-python/pull/1605
* Add a warning if user orders in a POD that is being closed by @caberos in https://github.com/softlayer/softlayer-python/pull/1600
* updated number of updates in the command account event-detail by @edsonarios in https://github.com/softlayer/softlayer-python/pull/1609
* Add an orderBy filter to slcli vlan list by @caberos in https://github.com/softlayer/softlayer-python/pull/1599
* Add options to print a specific table in command slcli account events by @edsonarios in https://github.com/softlayer/softlayer-python/pull/1611
* Update global ip assign/unassign to use new API by @caberos in https://github.com/softlayer/softlayer-python/pull/1614
* Ability to route/unroute subnets by @caberos in https://github.com/softlayer/softlayer-python/pull/1615
* Improved successful response to command - slcli account cancel-item by @edsonarios in https://github.com/softlayer/softlayer-python/pull/1617
* Improved successful response to command - slcli virtual edit by @edsonarios in https://github.com/softlayer/softlayer-python/pull/1618
* Improved successful response to command - slcli vlan cancel by @edsonarios in https://github.com/softlayer/softlayer-python/pull/1619
* Mishandling of domain and hostname data in `slcli account item-detail` by @edsonarios in https://github.com/softlayer/softlayer-python/pull/1621
* Unable to get VSI details when last TXN is "Software install is finis… by @caberos in https://github.com/softlayer/softlayer-python/pull/1625
* new command on autoscale delete by @caberos in https://github.com/softlayer/softlayer-python/pull/1628
* Incorrect table title is displayed when an Auto Scale Group is scaled to reduce members by @BrianSantivanez in https://github.com/softlayer/softlayer-python/pull/1629
* slcli autoscale create by @caberos in https://github.com/softlayer/softlayer-python/pull/1623
* Soap transport by @allmightyspiff in https://github.com/softlayer/softlayer-python/pull/1626
* fix issue on loadbal order command by @caberos in https://github.com/softlayer/softlayer-python/pull/1633
* Policy is not added when an AutoScale Group is created by @caberos in https://github.com/softlayer/softlayer-python/pull/1637
* When `slcli event-log` not return any event log the command display an error by @BrianSantivanez in https://github.com/softlayer/softlayer-python/pull/1641
* add new columns on vlan list(premium, tags) by @caberos in https://github.com/softlayer/softlayer-python/pull/1645
* fixed documentation build issues by @allmightyspiff in https://github.com/softlayer/softlayer-python/pull/1648
* Improved successful response to command - slcli licenses cancel by @edsonarios in https://github.com/softlayer/softlayer-python/pull/1653
* update the firewall list by @caberos in https://github.com/softlayer/softlayer-python/pull/1649
* Updated readme by @allmightyspiff in https://github.com/softlayer/softlayer-python/pull/1656
* Update `slcli firewall detail` to handle multi vlan firewalls by @BrianSantivanez in https://github.com/softlayer/softlayer-python/pull/1651
* New command for getting duplicate convert status  by @ko101 in https://github.com/softlayer/softlayer-python/pull/1655
* Fixed TOX errors by @allmightyspiff in https://github.com/softlayer/softlayer-python/pull/1661
* add a new feature to get all cloud object storage by @caberos in https://github.com/softlayer/softlayer-python/pull/1662
* Update `slcli report bandwidth` command by @BrianSantivanez in https://github.com/softlayer/softlayer-python/pull/1664
* add firewall monitoring command by @caberos in https://github.com/softlayer/softlayer-python/pull/1657
* add a new command on block object-storage details by @caberos in https://github.com/softlayer/softlayer-python/pull/1666
* slcli account bandwidth-pools-detail command displays an error with b… by @caberos in https://github.com/softlayer/softlayer-python/pull/1670
* new feature block object-storage permissions command by @caberos in https://github.com/softlayer/softlayer-python/pull/1668
* fix the vlan table by @caberos in https://github.com/softlayer/softlayer-python/pull/1672

#### New Contributors
* @BrianSantivanez made their first contribution in https://github.com/softlayer/softlayer-python/pull/1629

**Full Changelog**: https://github.com/softlayer/softlayer-python/compare/v6.0.2...v6.1.0


### [6.0.2] - 2022-03-30

#### What's Changed
* New Command slcli hardware|virtual monitoring by @caberos in https://github.com/softlayer/softlayer-python/pull/1593
* When listing datacenters/pods, mark those that are closing soon. by @caberos in https://github.com/softlayer/softlayer-python/pull/1597


**Full Changelog**: https://github.com/softlayer/softlayer-python/compare/v6.0.1...v6.0.2

## [6.0.1] - 2022-03-11


#### What's Changed
* Replace the use of ptable with prettytable by @dvzrv in https://github.com/softlayer/softlayer-python/pull/1584
* Bandwidth pool management by @caberos in https://github.com/softlayer/softlayer-python/pull/1582
* Add id in the result in the command bandwidth-pools by @edsonarios in https://github.com/softlayer/softlayer-python/pull/1586
* Datacenter closure report by @allmightyspiff in https://github.com/softlayer/softlayer-python/pull/1592
* fix to errors in slcli hw create-options by @caberos in https://github.com/softlayer/softlayer-python/pull/1594


**Full Changelog**: https://github.com/softlayer/softlayer-python/compare/v5.9.9...v6.0.1

6.0.0 was skipped.

## [5.9.9] - 2022-02-04

https://github.com/softlayer/softlayer-python/compare/v5.9.8...v5.9.9

#### Improvements
- Add loadbalancer timeout values #1576
- Add pricing date to slcli order preset-list #1578

#### New Commands
- `slcli vlan create-options` add new feature on vlan #1572
- `slcli account bandwidth-pools` Bandwidth pool features #1579

## [5.9.8] - 2021-12-07

https://github.com/softlayer/softlayer-python/compare/v5.9.7...v5.9.8

#### Improvements

- Fix code blocks formatting of The Solution section docs #1534
- Add retry decorator to documentation #1535
- Updated utility docs #1536
- Add Exceptions to Documentation #1537
- Forces specific encoding on XMLRPC requests #1543
- Add sensor data to hardware #1544
- Ignoring f-string related messages for tox for now #1548
- Fix account events #1546
- Improved loadbal details #1549
- Fix initialized accountmanger #1552
- Fix hw billing reports 0 items #1556
- Update API docs link and remove travisCI mention #1557
- Fix errors with vs bandwidth #1563
- Add Item names to vs billing report #1564
- Mapping is now in collections.abc #1565
- fix vs placementgroup list #1567
- fixed up snapshot-notification cli commands #1569

#### New Commands
- loadbal l7policies #1553
    + ` slcli loadbal l7policies --protocol-id`
    + `slcli loadbal l7policies`
- Snapshot notify #1554
    + `slcli file|block snapshot-set-notification`
    + `slcli file|block snapshot-get-notification-status`



## [5.9.7] - 2021-08-04
https://github.com/softlayer/softlayer-python/compare/v5.9.6...v5.9.7

#### Improvements
- Fixed some doc block issues when generating HTML #1513
- Updates to the Release workflow for publishing to test pypi #1514

- Adding in CodeQL Analysis #1517
- Create SECURITY.md #1518
- Fix the network space is empty on subnet detail #1523
- Prevents SLCLI_VERSION environment variable from breaking things #1527
- Refactor loadbal order-options #1521
- slcli server create-options dal13 Error #1526

#### New Commands
- add new feature on vlan cli #1499
    + `slcli vlan create`

## [5.9.6] - 2021-07-05
https://github.com/softlayer/softlayer-python/compare/v5.9.5...v5.9.6

#### Improvements
- Updated snap to core20 and edited README #1494
- Add a table result for `slcli hw upgrade` output. #1488
- Remove block/file interval option for replica volume. #1497
- `slcli vlan cancel` should report if a vlan is automatic. #1495
- New method to manage how long text is in output tables. #1506
- Fix Tox-analysis issues. #1510

#### New Commands
- add new email feature #1483
    + `slcli email list`
    + `slcli email detail`
    + `slcli email edit`
- `slcli vlan cancel`
- Add slcli account licenses #1501
    + `slcli account licenses`
- Create a new commands on slcli that create/cancel a VMware licenses #1504
    + `slcli licenses create`
    + `slcli licenses cancel`


## [5.9.5] - 2021-05-25
https://github.com/softlayer/softlayer-python/compare/v5.9.4...v5.9.5

#### Improvements
- Changed a testing domain to one that really doesnt exist #1492
- Fix Incomplete notes field for file and block #1484
- Show component versions on hw detail #1470
- Add the firewall information on slcli firewall detail #1475
- Add an --orderBy parameters to call-api #1459
- Add image detail transaction data #1479



## [5.9.4] - 2021-04-27
https://github.com/softlayer/softlayer-python/compare/v5.9.3...v5.9.4

#### New Commands
- `slcli hw authorize-storage`  #1439
- `slcli order quote-save` #1451


#### Improvements

- Refactored managers.ordering_manager.verify_quote() to work better with the REST endpoing #1430
- Add routers for each DC in slcli hw create-options #1432
- Add preset datatype in slcli virtual detail #1435
- Add upgrade option to slcli hw. #1437
- Ibmcloud authentication support #1315 / #1447
  + `slcli config setup --ibmid`
  + `slcli config setup --sso`
  + `slcli config setup --cloud_key`
  + `slcli config setup --classic_key`
- Refactor slcli hw detail prices. #1443
- Updated contributing guide #1458
- Add the Hardware components on "slcli hardware detail" #1452
- Add billing and lastTransaction on hardware detail #1446
- Forced reserved capacity guests to be monthly #1454
- Removing the rwhois commands #1456
- Added automation to publish to test-pypi #1467
- Updating author_email to SLDN distro list #1469
- Add the option to add and upgrade the hw disk. #1455
- Added a utility to merge objectFilters, #1468
- Fixes shift+ins when pasteing into a password field for windows users. #1460
- Add Billing and lastTransaction on slcli virtual detail #1466
- Fixing 'import mock' pylint issues #1476


## [5.9.3] - 2021-03-03
https://github.com/softlayer/softlayer-python/compare/v5.9.2...v5.9.3

#### New Commands
- `slcli file|block disaster-recovery-failover` #1407

#### Improvements
- Unit testing for large integers #1403
- Add Multi factor authentication to users list #1408
- Add pagination to object storage list accounts. #1411
- Add username lookup to slcli object-storage credential #1415
- Add IOPs data to slcli block volume-list. #1418
- Add 2FA and classic APIKeys fields to slcli user list as default values #1421
- Add a flags in the report bandwidth #1420
- Add the option network component by router to slcli hw create. #1422
- Add slcli vs create by router data. #1414
- Add testing and support for python 3.9. #1429
- Checking for TermLength on prices #1428



## [5.9.2] - 2020-12-03
https://github.com/softlayer/softlayer-python/compare/v5.9.1...v5.9.2

#### New Commands
-  `slcli account orders` #1349
-  `slcli order lookup` #1354

#### Improvements
- Ordering price information improvements. #1319
- refactor vsi create-option #1337
- Add Invoice Item id as parameter in `slcli account item-detail` command
- Added order lookup command to block and file orders. #1350
- Add prices to vs create-options. #1351
- Allow orders without a location if needed #1356
- Refactor file and block commands to use the username resolver #1357
- Fix create subnet static for ipv4 price. #1358
- moved snapcraft readme #1363
- Update snapcraft.yaml #1365
- Updated documentation on how to deal with KeyError #1366
- Fix order item-list --prices location #1360
- Removed Nessus scanner from docs and examples #1368
- Fix subnet list. #1379
- Fixed analysis/flake8 tests #1381
- Remove the `-a` option from `slcli user create`. Only the user themselves can create an API key now. #1377

## [5.9.1] - 2020-09-15
https://github.com/softlayer/softlayer-python/compare/v5.9.0...v5.9.1

- Fix the ha option for firewalls, add and implement unit test #1327
- BluePages_Search and IntegratedOfferingTeam_Region don't need SoftLayer_ prefix #972
- Fix new TOX issues #1330
- Add more unit test coverage #1331
- Set notes for network storage #1322
- Some improvements to the dns commands #999
  + dns zone-list: added resourceRecordCount, added automatic pagination for large zones
  + dns record-list: fixed an issue where a record (like SRV types) that don't have a host would cause the command to fail
- Renamed managers.storage.refresh_dep_dupe to  SoftLayer.managers.storage.refresh_dupe #1342 to support the new API method. CLI commands now use this method.
- #1295 added disk upgrade options for virtual guests

## [5.9.0] - 2020-08-03
https://github.com/softlayer/softlayer-python/compare/v5.8.9...v5.9.0

- #1280 Notification Management
  + slcli user notifications
  + slcli user edit-notifications
- #828 Added networking options to slcli hw create-options
  + Refactored slcli hw create to use the ordering manager
  + Added --network option to slcli hw create for more granular network choices.
  + Deprecated --port-speed and --no-public . They still work for now, but will be removed in a future release.
- #1298 Fix Unhandled exception in CLI - vs detail
- #1309 Fix the empty lines in slcli vs create-options
- #1301 Ability to list VirtualHost capable guests
  + slcli hardware guests
  + slcli vs list will show guests on VirtualHost servers
- #875 added option to reload bare metal servers with LVM enabled
- #874 Added Migrate command
- #1313 Added support for filteredMask
- #1305 Update docs links
- #1302 Fix lots of whitespace slcli vs create-options
- #900 Support for STDIN on creating and updating tickets.
- #1318 add Drive number in guest drives details using the device number
- #1323 add vs list hardware and all option

## [5.8.9] - 2020-07-06
https://github.com/softlayer/softlayer-python/compare/v5.8.8...v5.8.9

- #1252 Automated Snap publisher
- #1230 Tag Management
    + slcli tags cleanup
    + slcli tags delete
    + slcli tags details
    + slcli tags list
    + slcli tags set
    + slcli tags taggable
- #1285 Vlan editing functionality
- #1287 Edit IP note and add ipAddress table in detail view
- #1283 Subnet Tagging
- #1291 Storage documentation updates
- #1293 add system operation referenceCode in create-option

## [5.8.8] - 2020-05-18
https://github.com/softlayer/softlayer-python/compare/v5.8.7...v5.8.8

- #1266 Fixed ticket upload with REST endpoint
- #1263 add the redundant/degraded option to hardware
- #1262 Added `iter` option for ordering manager functions
- #1264 Add Account planned, unplanned and announcement events
- #1265 fixed pylint 2.5.0 errors 
- #1261 Fix AttributeError: 'NoneType' object has no attribute 'keys 
- #1256 Adding more github action tests, removing travis CI tests 
- #887 fix Response shows additional new lines (\n) in ticket details
- #1241 Storage feature for virtual and hardware servers 
- #1242 Hardware and Virtual billing info
- #1239 VPN subnet access to a use
- #1254 added account billing-items/item-details/cancel-item commands

## [5.8.7] - 2020-03-26
https://github.com/softlayer/softlayer-python/compare/v5.8.5...v5.8.7

- #1222 Get load balancer (LBaaS) by name
- #1221 Added version checker
- #1227 Updated unit test suite for TravisCI to run properly
- #1225 Add note about using multiple colon symbols not working when setting tags.
- #1228 Support ordering [Dependent Duplicate Volumes](https://cloud.ibm.com/docs/BlockStorage?topic=BlockStorage-dependentduplicate)
- #1233 Refactored File/Block managers to reduce duplicated code.
- #1231 Added Refresh functions for Dependent Duplicate Volumes
- #801 Added support for JSON styled parameters and object filters
- #1234 Added ability to change which datacenters an image template was stored in

## [5.8.6] - Skipped

## [5.8.5] - 2020-01-29
https://github.com/softlayer/softlayer-python/compare/v5.8.4...v5.8.5

-  #1195 Fixed an issue with `slcli vs dns-sync --ptr`. Added `slcli hw dns-sync`
-  #1199 Fix File Storage failback and failover.
-  #1198 Fix issue where the summary command fails due to None being provided as the datacenter name.
-  #1208 Added The following commands:
    - `slcli block volume-limits` 
    - `slcli file  volume-limits`
- #1209  Add testing/CI for python 3.8.
- #1212 Fix vs detail erroring on servers pending cancellation.
- #1210 support subnet ACL management through cli
    + `slcli block subnets-list`
    + `slcli block subnets-assign`
    + `slcli block subnets-remove`
- #1215 Added documentation for all SLCLI commands.


## [5.8.4] - 2019-12-20
https://github.com/softlayer/softlayer-python/compare/v5.8.3...v5.8.4

- #1199 Fix block storage failback and failover.
- #1202 Order a virtual server private. 


## [5.8.3] - 2019-12-11
https://github.com/softlayer/softlayer-python/compare/v5.8.2...v5.8.3

- #771 Fixed unicode errors in image list (for windows)
- #1191 Fixed ordering virtual server dedicated from the CLI
- #1155 Fixed capacity restriction when ordering storage quotes
- #1192 Fixed hardware detail bandwidth allocation errors. 


## [5.8.2] - 2019-11-15
- https://github.com/softlayer/softlayer-python/compare/v5.8.1...v5.8.2


+ #1186 Fixed a unit test that could fail if the test took too long to run.
+ #1183 Added a check to ensure subnet and vlan options are properly added to the order for virtual servers.
+ #1184 Fixed a readme misspelling.
+ #1182 Fixed vs reboot unable to resolve vs names.
+ #1095 Handle missing Fixtures better for unit tests.

## [5.8.1] - 2019-10-11
- https://github.com/softlayer/softlayer-python/compare/v5.8.0...v5.8.1

+ #1169 Drop python 2.7 support
+ #1170 Added CS# to ticket listing
+ #1162 Fixed issue looking up OS keyName instead of referenceCode
+ #627 Autoscale support
    * slcli autoscale detail
    * slcli autoscale edit
    * slcli autoscale list
    * slcli autoscale logs
    * slcli autoscale scale
    * slcli autoscale tag

## [5.8.0] - 2019-09-04
- https://github.com/softlayer/softlayer-python/compare/v5.7.2...v5.8.0

+ #1143 Upgrade to prompt_toolkit >= 2
+ #1003 Bandwidth Feature
    * slcli summary
    * slcli report bandwidth
    * slcli vs bandwidth
    * slcli hw bandwidth
    * Added bandwidth to VS and HW details page
+ #1146 DOCS: replace 'developer' with 'sldn' links
+ #1147 property 'contents' is not valid for 'SoftLayer_Ticket' when creating a ticket
+ #1139 cannot create static subnet with slcli
+ #1145 Refactor cdn network.
+ #1152 IBMID auth support
+ #1153, #1052 Transient VSI support
+ #1167 Removed legacy LoadBalancer command, added Citrix and IBM LBaaS commands.
    * slcli lb cancel
    * slcli lb detail
    * slcli lb health
    * slcli lb l7pool-add
    * slcli lb l7pool-del
    * slcli lb list
    * slcli lb member-add
    * slcli lb member-del
    * slcli lb ns-detail
    * slcli lb ns-list
    * slcli lb order
    * slcli lb order-options
    * slcli lb pool-add
    * slcli lb pool-del
    * slcli lb pool-edit
+ #1157 Remove VpnAllowedFlag.
+ #1160 Improve hardware cancellation to deal with additional cases

## [5.7.2] - 2019-05-03
- https://github.com/softlayer/softlayer-python/compare/v5.7.1...v5.7.2

+ #1107 Added exception to handle json parsing error when ordering 
+ #1068 Support for -1 when changing port speed 
+ #1109 Fixed docs about placement groups
+ #1112 File storage endurance iops upgrade 
+ #1101 Handle the new user creation exceptions 
+ #1116 Fix order place quantity option
+ #1002 Invoice commands
    * account invoices
    * account invoice-detail
    * account summary
+ #1004 Event Notification Management commands
    * account events
    * account event-detail
+ #1117 Two PCIe items can be added at order time 
+ #1121 Fix object storage apiType for S3 and Swift.
+ #1100 Event Log performance improvements. 
+ #872 column 'name' was renamed to 'hostname'
+ #1127 Fix object storage credentials.
+ #1129 Fixed unexpected errors in slcli subnet create
+ #1134 Change encrypt parameters for importing of images. Adds root-key-crn
+ #208 Quote ordering commands
    * order quote
    * order quote-detail
    * order quote-list
+ #1113 VS usage information command
    * virtual usage 
+ #1131 made sure config_tests dont actually make api calls.


## [5.7.1] - 2019-02-26
- https://github.com/softlayer/softlayer-python/compare/v5.7.0...v5.7.1

+ #1089 removed legacy SL message queue commands
+ Support for Hardware reflash firmware CLI/Manager method

## [5.7.0] - 2019-02-15
- Changes: https://github.com/softlayer/softlayer-python/compare/v5.6.4...v5.7.0

+ #1099 Support for security group Ids
+ event-log cli command
+ #1069 Virtual Placement Group Support
   ```
      slcli vs placementgroup --help
    Commands:
      create          Create a placement group.
      create-options  List options for creating a placement group.
      delete          Delete a placement group.
      detail          View details of a placement group.
      list            List placement groups.
   ```
+ #962 Rest Transport improvements. Properly handle HTTP exceptions instead of crashing.
+ #1090 removed power_state column option from "slcli server list"
+ #676 - ipv6 support for creating virtual guests
  * Refactored virtual guest creation to use Product_Order::placeOrder instead of Virtual_Guest::createObject, because createObject doesn't allow adding IPv6
+ #882 Added table which shows the status of each url in object storage
+ #1085 Update provisionedIops reading to handle float-y values
+ #1074 fixed issue with config setup
+ #1081 Fix file volume-cancel
+ #1059 Support for SoftLayer_Hardware_Server::toggleManagementInterface
  * `slcli hw toggle-ipmi`


## [5.6.4] - 2018-11-16

- Changes: https://github.com/softlayer/softlayer-python/compare/v5.6.3...v5.6.4

+ #1041 Dedicated host cancel, cancel-guests, list-guests
+ #1071 added createDate and modifyDate parameters to sg rule-list
+ #1060 Fixed slcli subnet list
+ #1056 Fixed documentation link in image manager
+ #1062 Added description to slcli order 

## [5.6.3] - 2018-11-07

- Changes: https://github.com/softlayer/softlayer-python/compare/v5.6.0...v5.6.3

+ #1065 Updated urllib3 and requests libraries due to CVE-2018-18074
+ #1070 Fixed an ordering bug
+ Updated release process and fab-file

## [5.6.0] - 2018-10-16
- Changes: https://github.com/softlayer/softlayer-python/compare/v5.5.3...v5.6.0

+ #1026 Support for [Reserved Capacity](https://cloud.ibm.com/docs/virtual-servers?topic=virtual-servers-about-reserved-virtual-servers)
  * `slcli vs capacity create`
  * `slcli vs capacity create-guest`
  * `slcli vs capacity create-options`
  * `slcli vs capacity detail`
  * `slcli vs capacity list`
+ #1050 Fix `post_uri` parameter name on docstring
+ #1039 Fixed suspend cloud server order.
+ #1055 Update to use click 7
+ #1053 Add export/import capabilities to/from IBM Cloud Object Storage to the image manager as well as the slcli. 


## [5.5.3] - 2018-08-31
- Changes: https://github.com/softlayer/softlayer-python/compare/v5.5.2...v5.5.3

+ Added `slcli user delete`
+ #1023 Added `slcli order quote` to let users create a quote from the slcli.
+ #1032 Fixed vs upgrades when using flavors.
+ #1034 Added pagination to ticket list commands
+ #1037 Fixed DNS manager to be more flexible and support more zone types.
+ #1044 Pinned Click library version at >=5 < 7

## [5.5.2] - 2018-08-31
- Changes: https://github.com/softlayer/softlayer-python/compare/v5.5.1...v5.5.2

+ #1018 Fixed hardware credentials.
+ #1019 support for ticket priorities
+ #1025 create dedicated host with gpu fixed.


## [5.5.1] - 2018-08-06
- Changes: https://github.com/softlayer/softlayer-python/compare/v5.5.0...v5.5.1

- #1006, added paginations to several slcli methods, making them work better with large result sets. 
- #995, Fixed an issue displaying VLANs.
- #1011, Fixed an issue displaying some NAS passwords
- #1014, Ability to delete users

## [5.5.0] - 2018-07-09
- Changes: https://github.com/softlayer/softlayer-python/compare/v5.4.4...v5.5.0

- Added a warning when ordering legacy storage volumes
- Added documentation link to volume-order
- Increased slcli output width limit to 999 characters
- More unit tests
- Fixed an issue canceling some block storage volumes
- Fixed `slcli order` to work with network gateways
- Fixed an issue showing hardware credentials when they do not exist
- Fixed an issue showing addressSpace when listing virtual servers
- Updated ordering class to support baremetal servers with multiple GPU
- Updated prompt-toolkit as a fix for `slcli shell`
- Fixed `slcli vlan detail` to not fail when objects don't have a hostname
- Added user management


## [5.4.4] - 2018-04-18
- Changes: https://github.com/softlayer/softlayer-python/compare/v5.4.3...v5.4.4

- fixed hw list not showing transactions
- Re-factored RestTransport and XMLRPCTransport, logging is now only done in the DebugTransport
- Added print_reproduceable to XMLRPCTransport and RestTransport, which should be very useful in printing out pure API calls.
- Fixed an issue with RestTransport and locationGroupId


## [5.4.3] - 2018-03-30
 - Changes: https://github.com/softlayer/softlayer-python/compare/v5.4.2...v5.4.3

- Corrected to current create-options output
- Allow ordering of account restricted presets
- Added lookup function for datacenter names and ability to use `slcli order` with short DC names
- Changed locatoinGroupId to check for None instead of empty string
- Added a way to try to cancel montly bare metal immediately. THis is done by automatically updating the cancellation request. A human still needs to read the ticket and process it for the reclaim to complete.

## [5.4.2] - 2018-02-22
 - Changes: https://github.com/softlayer/softlayer-python/compare/v5.4.1...v5.4.2

- add GPU to the virtual create-options table
- Remove 'virtual' from the hardware ready command.
- Carefully check for the metric tracking id on virtual guests when building a bandwidth report.
- Do not fail if the source or destination subnet mask does not exist for ipv6 rules.

## [5.4.1] - 2018-02-05
 - Changes: https://github.com/softlayer/softlayer-python/compare/v5.4.0...v5.4.1

- Improve error conditions when adding SSH keys
- added type filters to package-list, auto-removes bluemix_services on package listing
- Add boot mode option to virtual guest creation
- Update documentation for security group rule add
- Add fix for unsetting of values in edit SG rules

## [5.4.0] - 2018-01-15
 - Changes: https://github.com/softlayer/softlayer-python/compare/v5.3.2...v5.4.0

 - Upgraded Requests and Urllib3 library to latest. This allows the library to make use of connection retries, and connection pools. This should prevent the client from crashing if the API gives a connection reset / connection timeout error
 - reworked wait_for_ready function for virtual, and added to hardware managers. 
 - fixed block/file iops in the `slcli block|file detail` view
 - Added sub items to `hw detail --price`, removed reverse PTR entries

### Added to CLI
- slcli order
```
$ ./slcli order
Usage: slcli order [OPTIONS] COMMAND [ARGS]...

Options:
  -h, --help  Show this message and exit.

Commands:
  category-list      List the categories of a package.
  item-list          List package items used for ordering.
  package-list       List packages that can be ordered via the...
  package-locations  List Datacenters a package can be ordered in.
  place              Place or verify an order.
  preset-list        List package presets.
```


## [5.3.2] - 2017-12-18
 - Changes: https://github.com/softlayer/softlayer-python/compare/v5.3.1...v5.3.2

 - Expanded `@retry` useage to a few areas in the hardware manager
 - Added INTERVAL options to block and file replication
 - Fixed pricing error on `hw detail --price`
 - Added sub items to `hw detail --price`, removed reverse PTR entries

### Added to CLI
- slcli dedicatedhost 


## [5.3.1] - 2017-12-07
 - Changes: https://github.com/softlayer/softlayer-python/compare/v5.3.0...v5.3.1
 - Added support for storage volume modifications

### Added to CLI
- slcli block volume-modify
- slcli file volume-modify

## [5.3.0] - 2017-12-01
 - Changes: https://github.com/softlayer/softlayer-python/compare/v5.2.15...v5.3.0
 - Added a retry decorator. currently only used in setTags for VSI creation, which should allos VSI creation to be a bit more robust.
 - Updated unit tests to work with pytest3.3

## [5.2.15] - 2017-10-30
 - Changes: https://github.com/softlayer/softlayer-python/compare/v5.2.14...v5.2.15
 - Added dedicated host info to virt detail
 - #885 - Fixed createObjects on the rest api endpoint
 - changed securityGroups to use createObject instead of createObjects
 - Always set the endpoint_url by defaulting to the public URL if the endpoint type cannot be determined.
 - resource metadata update

## [5.2.14] - 2017-09-13
 - Changes: https://github.com/softlayer/softlayer-python/compare/v5.2.13...v5.2.14
 - Improved slcli vs create-options output
 - Updated slcli vs create to support new virtual server public and dedicated host offerings

## [5.2.13] - 2017-09-05
 - Changes: https://github.com/softlayer/softlayer-python/compare/v5.2.12...v5.2.13
 - Support for hourly billing of storage
 - Added exception handling for Managers.VSManager.wait_for_ready()
 - Added windows support for unit testing
 - Updated pypy version
 
## [5.2.12] - 2017-08-09
 - Changes: https://github.com/softlayer/softlayer-python/compare/v5.2.11...v5.2.12
 - Support for storage_as_a_service block and file storage
 
#### Added to CLI
 - block volume-count
 - file volume-count
 - securitygroups
   - create            Create a security group.
   - delete            Deletes the given security group
   - detail            Get details about a security group.
   - edit              Edit details of a security group.
   - interface-add     Attach an interface to a security group.
   - interface-list    List interfaces associated with security...
   - interface-remove  Detach an interface from a security group.
   - list              List security groups.
   - rule-add          Add a security group rule to a security...
   - rule-edit         Edit a security group rule in a security...
   - rule-list         List security group rules.
   - rule-remove 

## [5.2.11] - 2017-08-04
 - Changes: https://github.com/softlayer/softlayer-python/compare/v5.2.10...v5.2.11
 - Sync VLAN and subnet detail CLI output

## [5.2.10] - 2017-07-27
 - Changes: https://github.com/softlayer/softlayer-python/compare/v5.2.9...v5.2.10
 - Avoid blindly passing memory result to formatter

## [5.2.9] - 2017-07-27
 - Changes: https://github.com/softlayer/softlayer-python/compare/v5.2.8...v5.2.9
 - Add support for dedicated host instances to virtual server upgrades
#### Added to CLI
* block volume-set-lun-id

## [5.2.8] - 2017-07-19
 - Changes: https://github.com/softlayer/softlayer-python/compare/v5.2.7...v5.2.8
 
 * Resolved https://github.com/softlayer/softlayer-python/issues/835
 * Resolved https://github.com/softlayer/softlayer-python/issues/826
 * Fix dedicated/private VSI price retrieval for upgrades
 
#### Added to CLI
* block access-password

## [5.2.7] - 2017-06-22
 - Changes: https://github.com/softlayer/softlayer-python/compare/v5.2.6...v5.2.7

Adds support for duplicating block and file storage volumes. Only works on Storage as a Service volumes (Volumes that support encryption at rest). 

#### Added to CLI
 * [block|file] volume-duplicate

## [5.2.6] - 2017-05-22
 - Changes: https://github.com/softlayer/softlayer-python/compare/v5.2.5...v5.2.6
 
#### Added To CLI
* ipsec list
* ipsec detail
* ipsec configure
* ipsec update
* ipsec subnet-add
* ipsec subnet-remove
* ipsec translation-add
* ipsec translation-remove
* ipsec translation-update


## [5.2.5] - 2017-05-05
 - Changes: https://github.com/softlayer/softlayer-python/compare/v5.2.1...v5.2.5
 
The SoftLayer_Network_Storage::storageTierLevel relational property changed in https://softlayer.github.io/release_notes/20170503/ , this version fixes problems caused by that.

### Changed
 - https://github.com/softlayer/softlayer-python/issues/818
 - https://github.com/softlayer/softlayer-python/pull/817
 
## [5.2.4] - 2017-04-06
 - Changes: https://github.com/softlayer/softlayer-python/compare/v5.2.3...v5.2.4
 
### Changed
Removed some debug code that was accidently added in the pypi release
 
## [5.2.3] - 2017-04-05
 - Changes: https://github.com/softlayer/softlayer-python/compare/v5.2.2...v5.2.3

### Added
 - Adds Python 3.6 support

### Changed
 - CLI+API: Removes the iSCSI manager and commands
 - API: Fixes hardware order failing to find a single bare metal fast provision package to use

## [5.2.2] - 2017-02-24
 - Changes: https://github.com/softlayer/softlayer-python/compare/v5.2.1...v5.2.2

### Added
 - Adds release process documentation
 - CLI: Displays NFS mount point for volumes in volume list and detail commands
 - CLI+API: Enables `slcli file` and `block` storage commands to order tier 10 endurance storage and replica

### Changed
 - Updates docs to replace `sl` command with `slcli`
 - CLI: Removes requirement to have `--os-type` provided for file storage ordering
 - API: Fixes block storage ordering to handle size provided properly
 - CLI: Fixes load balancer detail output so that JSON output is sane
 - API: Includes check if object storage endpoints were provided by the API before trying to add them to the endpoints returned by `list_endpoints`

## [5.2.1] - 2016-10-4
 - Changes: https://github.com/softlayer/softlayer-python/compare/v5.2.0...v5.2.1

### Added
 - CLI: Adds a new 'jsonraw' format option that will print JSON without whitespace. This is useful for integrating the CLI with other tooling.

### Changed
 - API: Fixes JSON loading while using the REST transport with Python 3
 - CLI+API: Metadata disks are now excluded when capturing "all" block devices with `slcli virtual capture --all`
 - CLI: Fixes a bug where dns zone importing was not importing wildcard records

## [5.2.0] - 2016-08-25
 - Changes: https://github.com/softlayer/softlayer-python/compare/v5.1.0...v5.2.0

### Added
 - CLI+API: Significant additions to `slcli file` and `slcli block` commands. You can now authorize hosts, revoke access. You can also create, delete, restore, disable, enable snapshots. These features need to be battle-tested so report any issues that you see.
 - CLI+API: Adds logic to `SoftLayer.create_client_from_env` that detects if a REST endpoint_url was given in order to use the REST transport automatically. This means that you can also configure REST endpoints for `slcli`. The default still uses XML-RPC endpoint, but from a small amount of testing shows that the REST transport is significantly faster.
 - CLI: Adds `--network-space` to `slcli subnet list` in order to filter subnets based on network space. The two main options are PUBLIC and PRIVATE. For example, to list all public subnets, you can run: `slcli subnet list --network-space=PUBLIC`
 - CLI: Adds a new, non-default column, "created_by" that shows who ordered the volume for `slcli file volume-list` and `slcli block volume-list`.
 - CLI: Adds a new `slcli report bandwidth` command that will print a report of all bandwidth pools and virtual/hardware servers that your user has access to.
 - CLI: Adds an "IN" syntax to the `slcli call-api` command. For example, to find VSIs that are in either the dal05 or sng01 datacenter you can run this command: `slcli call-api Account getVirtualGuests -f 'virtualGuests.datacenter.name IN dal05,sng01'`

### Changed
 - CLI: Fixes a UnicodeEncodeError when piping slcli output with unicode characters. This was mostly reported with `slcli image list` but could also happen with many other calls.
 - CLI: Fixed a bug where os_version was not displaying correctly in `slcli virtual detail` or `slcli virtual detail`

## [5.1.0] - 2016-05-12
 - Changes: https://github.com/softlayer/softlayer-python/compare/v5.0.1...v5.1.0

### Added
 - CLI+API: Added block storage functionality. You can order, list, detail, cancel volumes. You can list and delete snapshots. You can also list ACLs for volumes.
 - Added functionality to attach/detach devices to tickets
 - CLI: Virtual list now lists users and passwords for all known software

### Changed
 - CLI: Fixes bug with `vlan detail` CLI command

## [5.0.1] - 2016-03-30
 - https://github.com/softlayer/softlayer-python/compare/v5.0.0...v5.0.1

### Changed
 - CLI: Adds missing dependency that was previously pulled in by prompt_toolkit
 - API: Fix a bug by updating the CDN manager to use the new purge method
 - CLI: Fixes bug that occured when iscsi listings with resources have no datacenter

## [5.0.0] - 2016-03-18
 - Changes: https://github.com/softlayer/softlayer-python/compare/v4.1.1...v5.0.0

### Added
 - CLI: Adds a shell (accessable with `slcli shell`) which provides autocomplete for slcli commands and options
 - CLI: How filters work with `slcli call-api` has changed significantly. Instead of accepting JSON, it now accepts an easier-to-use format. See `slcli call-api -h` for examples
 - API: Adds manager for object storage
 - API: Improved REST transport support

### Changed
 - CLI: Move modifying nic speed to `slcli virtual edit` and `slcli hardware edit` instead of having its own command
 - CLI: 'virtual' and 'hardware' are preferred over 'vs' and 'server' in the CLI
 - CLI+API: Many unmentioned bug fixes

## [4.1.1] - 2015-08-17
 - Changes: https://github.com/softlayer/softlayer-python/compare/v4.1.0...v4.1.1

### Added
 - CLI: Re-adds `--no-public` option to only provision private interfaces with servers via `slcli server create`

### Changed
 - CLI: Fixes to work with Click v5
 - Removes non-functional `--vlan-public` and `--vlan-private` from `slcli server create`
 - VSManager.wait_for_ready will now behave as it is documented to behave.

## [4.1.0] - 2015-08-17
 - Changes: https://github.com/softlayer/softlayer-python/compare/v4.0.4...v4.1.0

### Added
 - CLI: Adds a shell which provides a shell interface for `slcli`. This is available by using `slcli shell`
 - CLI: `slcli vs create` and `slcli server create` will now prompt for missing required options
 - CLI+API: Adds editing of hardware tags

### Changed
 - CLI: Fixes `slcli firewall add` command
 - CLI: Handles case where `slcli vs detail` and `slcli server detail` was causing an error when trying to display the creator
 - API: Fixes VSManager.verify_create_instance() with tags (and, in turn, `slcli vs create --test` with tags)
 - CLI: Fixes `vs resume` command
 - API+CLI: Updates hardware ordering to deal with location-specific prices
 - CLI: Fixes several description errors in the CLI
 - CLI: Running `vs edit` without a tag option will no longer remove all tags

## [4.0.4] - 2015-06-30
 - Changes: https://github.com/softlayer/softlayer-python/compare/v4.0.3...v4.0.4

### Changed
 - CLI: Fixes bug with pulling the userData property for the virtual server detail
 - CLI: Fixes a class of bugs invloving unicode from the API

## [4.0.3] - 2015-06-15
 - Changes: https://github.com/softlayer/softlayer-python/compare/v4.0.2...v4.0.3

### Changed
 - CLI: Fixes bug with `slcli vs ready` command
 - CLI: Fixes bug with `slcli loadbal service-add` command
 - CLI: Fixes bug with `slcli vlan list` with vlans that don't have a datacenter
 - CLI: Improves validation of virtual server and hardware create commands

## [4.0.2] - 2015-05-04
 - Changes https://github.com/softlayer/softlayer-python/compare/v4.0.1...v4.0.2

### Changed
 - CLI: Fixes a bug that breaks user confirmation prompts
 - CLI: Fixes general issue with sorting on certain row types in the CLI
 - API: Fixes image capture for Windows guests

## [4.0.1] - 2015-04-28
 - Changes: https://github.com/softlayer/softlayer-python/compare/v4.0.0...v4.0.1

### Changed
 - CLI: Fixes bug in `sl setup` command not properly defaulting to current values.
 - API: Fixes bug where turning off compression headers would still send compression headers.
 - CLI: Reverts to using ids over global identifiers for `sl vs list` and `sl server list`.

## [4.0.0] - 2015-04-21
 - Changes: https://github.com/softlayer/softlayer-python/compare/v3.3.0...v4.0.0
 - Because there are many changes between version 3 and version 4, it is strongly recommend to pin the version of the SoftLayer python bindings as soon as you can in order to prevent unintentional breakage when upgrading. To keep yourself on version 3, you can use this directive: softlayer>=3,<4. That can be used with pip (pip install softlayer>=3,<4), requirements in your setup.py and/or in your requirements.txt file.

### Added
 - API: The client transport is now pluggable. If you want to add extra logging or accounting, you can now subclass or wrap softlayer.transports.XmlRpcTransport in order to do so. A good example of that is done with softlayer.transports.TimingTransport.
 - API+CLI: Adds ability to import virtual images from a given URI. The API only supports importing from a swift account using 'swift://'. For more details, see http://developer.softlayer.com/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/createFromExternalSource.
 - CLI: A `--fixtures` global flag was added to pull from fixture data instead of the API. This is useful for discovery, demonstration and testing purposes.
 - CLI: A `--verbose` or `-v` flag was added to eventually replace `--debug`. To make a command more verbose, simply add more `-v` flags. For example `sl -vvv vs list` will be the most verbose and show everything down to request/response tracing.
 - CLI: Credentials can now be requested using `sl vs credentials <identifier>`, `sl hardware credentials <identifier>` and `sl nas credentials <identifier>` for virtual servers, hardware servers and NAS accounts respectively.
 - CLI: Adds virtual server rescue command, `sl vs rescue <identifier>`

### Changed
 - CLI: The command is renamed from `sl` to `slcli` to avoid package conflicts.
 - CLI: Global options now need to be specified right after the `slcli` command. For example, you would now use `slcli --format=raw list` over `slcli vs list --format=raw`. This is a change for the following options:
   - --format
   - -c or --config
   - --debug
   - --proxy
   - -y or --really
   - --version
 - API: The hardware manager has a significant update to how place_order() works. It will now only support the fast server provisioning package which has presets for options like CPU, Memory and disk.
 - API: Removed deprecated SoftLayer.CCIManager.
 - API: Adds virtual server rescue command to SoftLayer.VSManager
 - CLI: Significant changes were done to the CLI argument parsing. Docopt was dropped in favor of click. Therefore, some subtle differences which aren't documented here may exist.

## [3.3.0] - 2014-10-23
 - Changes: https://github.com/softlayer/softlayer-python/compare/v3.2.0...v3.3.0

### Added
 - CLI+API: Load balancer support
 - CLI: More detail added to the `sl image detail` and `sl image list` commands
 - CLI: Adds command to import DNS entries from BIND zone files
 - CLI+API: Adds support for booting into rescue images for virtual servers and hardware
 - API: Adds ability to order virtual and hardare servers from a quote to the ordering manager

### Changed
 - CLI: Fixes bug with `sl server list-chassis` and `sl server list-chassis`
 - API: Restructure of the way custom authentication can be plugged in the API client
 - Several other bug fixes

## [3.2.0] - 2014-07-09
 - Changes: https://github.com/softlayer/softlayer-python/compare/v3.1.0...v3.2.0

### Added
 - CLI+API: Added firewall manager and CLI module
 - CLI+API: Added iscsi manager and CLI module
 - API: Added ability to create multiple virtual servers at once to VSManager
 - API: Added OrderingManager. Remove hard-coded price IDs

### Changed
 - Fixed several small bugs

## [3.1.0] - 2014-04-24
 - Changes: https://github.com/softlayer/softlayer-python/compare/v3.0.2...v3.1.0

### Added
 - CLI+API: Added CDN manager and CLI module
 - CLI+API: Added ticket manager and CLI module
 - CLI+API: Added image manager and improves image CLI module
 - CLI+API: Added the ability to specify a proxy URL for API bindings and the CLI
 - CLI+API: Added ability to resize a virtual machine
 - CLI+API: Added firewall manager and CLI module
 - CLI+API: Added load balancer manager and CLI module

### Changed
 - API: six is now used to provide support for Python 2 and Python 3 with the same source
 - CLI+API: Implemented product name changes in accordance with SoftLayer's new product names. Existing managers should continue to work as before. Minor CLI changes were necessary.
 - Many bug fixes and minor suggested improvements

## [3.0.2] - 2013-12-9
 - Changes: https://github.com/softlayer/softlayer-python/compare/v3.0.1...v3.0.2

### Added
 - CLI+API: Simplified object mask reformatting and added support for more complex masks.
 - CLI+API: Added IPMI IP address to hardware details.
 - CLI: Added support for ordering multiple disks when creating a CCI.
 - API: Added flag to disable compression on HTTP requests.
 - CLI: Added CIDR information to subnet displays.

### Changed
 - CLI: Fixed the sl bmc create --network argument.
 - CLI+API: Improved output of the message queue feature and fixed some minor bugs.
 - CLI: Fixed an error when using --test and ordering a non-private subnet.
 - API: Fix to prevent double counting results in summary_by_datacenter().

### [3.0.1] - 2013-10-11
 - Changes: https://github.com/softlayer/softlayer-python/compare/v3.0.0...v3.0.1

### Added
 - CLI+API: Added ability to specify SSH keys when reloading CCIs and servers.

### Changed
 - CLI: Fixed an error message about pricing information that appeared when ordering a new private subnet.

## [3.0.0] - 2013-09-19
 - Changes: https://github.com/softlayer/softlayer-python/compare/v2.3.0...v3.0.0

### Added
 - CLI+API: Adds SoftLayer Message Queue Service bindings (as a manager) and a CLI counterpart. With this you can interact with existing message queue accounts
 - CLI+API: Adds the ability to create CCIs with the following options: metadata, post-install script, SSH key
 - CLI+API: Improved dedicated server ordering. Adds power management for hardware servers: power-on, power-off, power-cycle, reboot
 - CLI+API: Adds a networking manager and adds several network-related CLI modules. This includes the ability to:
   - list, create, cancel and assign global IPs
   - list, create, cancel and detail subnets. Also has the ability to lookup details about an IP address with 'sl subnet lookup'
   - list, detail VLANs
   - show and edit RWhois data
 - CLI+API: Ability to manage SSH Keys with a manager and a CLI module
 - CLI: Adds a --debug option to print out debugging information. --debug=3 is the highest log level which prints full HTTP request/responses including the body
 - CLI+API: Adds the ability to create hardware servers with a default SSH key
 - CLI: Adds templating for creating CCIs and hardware nodes which can be used to create more CCIs and hardware with the same settings

### Changed
 - Many bug fixes and consistency improvements
 - API: Removes old API client interfaces which have been deprecated in the v2. See link for more details: https://softlayer-api-python-client.readthedocs.org/en/latest/api/client/#backwards-compatibility
 - CLI: The commands in the main help are now organized into categories

## [2.3.0] - 2013-07-19
 - Changes: https://github.com/softlayer/softlayer-python/compare/v2.2.0...v2.3.0

### Added
 - CLI+API: Added much more hardware support: Filters for hardware listing, dedicated server/bare metal cloud ordering, hardware cancellation
 - CLI+API: Added DNS Zone filtering (server side)
 - CLI+API: Added Post Install script support for CCIs and hardware
 - CLI: Added Message queue functionality
 - CLI: Added --debug option to CLI commands
 - API: Added more logging
 - API: Added token-based auth so you can use the API bindings with your username/password if you want. (It's still highly recommended to use your API key instead of your password)

### Changed
 - Several bug fixes and improvements
 - Removed Python 2.5 support. Some stuff MIGHT work with 2.5 but it is no longer tested
 - API: Refactored managers into their own module to not clutter the top level

## [2.2.0] - 2013-04-11
### Added
 - Added sphinx documentation. See it here: https://softlayer-api-python-client.readthedocs.org
 - CCI: Adds Support for Additional Disks
 - CCI: Adds a way to block until transactions are done on a CCI
 - CLI: For most CCI commands, you can specify id, hostname, private ip or public ip as <identifier>
 - CLI: Adds the ability to filter list results for CCIs
 - API: for large result sets, requests can now be chunked into smaller batches on the server side. Using service.iter_call('getObjects', ...) or service.getObjects(..., iter=True) will return a generator regardless of the results returned. offset and limit can be passed in like normal. An additional named parameter of 'chunk' is used to limit the number of items coming back in a single request, defaults to 100

### Changed
 - Consistency changes/bug fixes
