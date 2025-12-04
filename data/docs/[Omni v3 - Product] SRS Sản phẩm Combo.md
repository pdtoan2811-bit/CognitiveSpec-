C:\\Users\\Sapoer\\Downloads\\Screenshot - 2020-02-01T105026.376.png

PHÂN TÍCH YÊU CẦU Quản lý sản phẩm Combo

Tháng 2, 2023 \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

1\. Mục đích 3 2. Phạm vi ảnh hưởng 3 3. Khái niệm, định nghĩa 3 4. Tài
liệu liên quan 3 5. Tổng quan mô hình sản phẩm 4 6. Nghiệp vụ sản phẩm
Combo 5 6.1. Quản lý thông tin Combo 5 a. Yêu cầu nghiệp vụ 6 b. Thông
tin combo_item 6 6.2. Tạo combo item gắn với phiên bản 7 6.3. Update
combo gắn với phiên bản combo 8 6.4. Xóa thành phần trong combo 8 6.5.
Xóa phiên bản sản phẩm tác động đến combo 9 6.6. 10 6.7. Thông tin kho
với sản phẩm combo 10 a. User story 10 b. Thông tin kho của combo 10 c.
Số lượng tồn kho của combo 11 7. Tạo Đơn hàng/Checkout với combo 13 7.1.
Các vấn đề 13 7.2. Định hướng 13 7.3. Tạo đơn hàng với combo 13 7.4. Tạo
checkout với combo 15 7.5. Ghi nhận giá trị combo trong order/checkout
16 8. Báo cáo 18 8.1. Báo cáo tồn kho 18 8.2. Báo cáo bán hàng 18 9. Mô
tả giao diện 19 9.1. Thêm mới sản phẩm combo 19 Ghi nhận thông tin
resource Product 20 Ghi nhận thông tin resource Combo 22 9.2. Chỉnh sản
phẩm combo 23 Chỉnh sửa thành phần combo 23 Chỉnh sửa thông tin combo 24

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

1\. Mục đích \* Là chủ cửa hàng, tôi muốn quản lý sản phẩm theo combo 2.
Phạm vi ảnh hưởng \* Module Sản phẩm \* Storefront Web \* Module Đơn
hàng - Checkout \* Module Tồn kho \* Module Báo cáo 3. Khái niệm, định
nghĩa STT Ký tự Diễn giải 1 KH Khách hàng: chủ cửa hàng, nhân viên, các
đối tượng sử dụng phần mềm để thực hiện các công việc 2 SP Sản phẩm

4\. Tài liệu liên quan STT Tên tài liệu Link 1 Wireframe
https://www.figma.com/file/gMKsj3IplGA7NdDes0uF7k/2.-Product?type=design&node-id=110%3A63532&mode=design&t=pQshOZpxSCwCWjMr-1
2 ERD

https://www.figma.com/file/PEjBdqGwJWWmCZ1aapRBno/%5BERD%5D-Product-Inventory?node-id=0%3A1&t=sCSKSFaVvjVaq1cs-1

3 SRS
https://docs.google.com/document/d/1-iFkJKD5_Oyy_yavSy40n_DMXmnmqiuxmMfddwtOIow/edit
4 API http://192.168.81.135:31006/?urls.primaryName=product_combos 5.
Tổng quan mô hình sản phẩm

Luồng nghiệp vụ:

Mô tả: Tên đối tượng

Mô tả Combo product.type: "combo" Là 1 hình thức quản lý sản phẩm trên
hệ thống omni 3 Combo item combo_item Các bản ghi thành phần combo của
một sản phẩm. Một sản phẩm có nhiều combo item (1:n)

6\. Nghiệp vụ sản phẩm Combo  1. Quản lý thông tin Combo

Là chủ cửa hàng, tôi muốn quản lý thông tin và bán sản phẩm combo 1. Yêu
cầu nghiệp vụ AC1: Sản phẩm combo là 1 sản phẩm có thông tin
product.type = combo để đánh dấu. Sản phẩm này có ít nhất 1 phiên bản là
combo AC2: Phiên bản combo là phiên bản có thông tin variant.type = true
để đánh dấu AC2: Khi tạo sản phẩm combo, mỗi thành phần trong combo sẽ
được ghi nhận thành một combo_item gắn với sản phẩm combo AC3: Giá combo
là giá của phiên bản sản phẩm gốc mà user add vào, API khởi tạo và cập
nhật combo sẽ hỗ trợ 3 loại tính giá khi gọi tới API combo: \*
combo_sum: giá phiên bản combo = Σ(giá combo_variant x số lượng trong
combo) \* fixed: giá cố định do user tự truyền \* None: giá của phiên
bản combo sẽ không được điều chỉnh AC4: Khi thay đổi giá phiên bản thành
phần, nếu không gọi API combo update =\> Hệ thống không tự động cập nhật
giá của combo AC5: Cho phép chỉnh sửa số lượng các phiên bản thành
phần + giá của combo AC6: Cho phép xóa phiên bản thành phần trong combo
AC7: Không cho phép phiên bản sản phẩm combo là combo_item của chính nó
=\> combo.variant_id phải khác combo_items.variant_id AC8: Không cho
phép chỉnh sửa kho sản phẩm combo\[a\] AC9: Không cho phép variant combo
là thành phần của 1 variant combo khác

2\. Thông tin combo_item no. field format required? edit? Note 1 id big
integer read-only Yes No Id duy nhất cho combo_item. 1 variant sẽ gắn
với n combo_item 2 parent\_ product_id big integer Yes Yes Id product
sản phẩm đại diện cho combo trong hệ thống Cho phép đổi thành phần trong
combo 3 parent\_ variant_id big integer Yes Yes Id variant mặc định sinh
ra bởi sản phẩm combo FE không cho phép tạo thêm phiên bản ngoài mặc
định với sản phẩm combo Cho phép đổi thành phần trong combo 3
combo_variant_id big integer Yes Yes Id phiên bản sản phẩm là thành phần
trong combo 4 combo_product_id big integer Yes Yes Id sản phẩm gắn với
phiên bản là thành phần trong combo 4 quantity Integer Yes Yes Số lượng
sản phẩm nằm trong combo Số nguyên trong API Max: 9,999,999 Lớn hơn 1 5
created_at datetime Yes No Thời gian hệ thống ghi nhận tạo ra 1 combo 6
updated_at datetime Yes Yes Thời gian hệ thống ghi nhận 1 thông tin của
combo được cập nhật 2. Tạo combo item gắn với phiên bản Điều kiện: \* Đã
có sản phẩm + phiên bản cha \* Cho phép sửa giá combo + sửa số lượng
phiên bản thành phần Method: POST a. Input Thông tin hệ thống Validate
required? Input Note Parent {} parent_product_id Big integer No ID sản
phẩm combo chứa các sản phẩm thành phần

parent_variant_id string Yes ID phiên bản combo chứa các sản phẩm thành
phần

calculate_type enum No Cách tính giá của sản phẩm combo combo_sum: giá
phiên bản combo = Σ(giá combo_variant x số lượng trong combo) Fixed: giá
cố định do user tự truyền \[b\]\[c\] price decimal No Giá sản phẩm combo
Max: 999,999,999 Min: 0 combo \[\] combo_varant_id Big integer Yes ID
phiên bản thành phần

quantity interger Yes Số lượng sản phẩm thành phần. Lớn hơn 0

b. Output \* Hệ thống tự tính toán giá của phiên bản combo và ghi nhận
vào variant.price = giá ghi nhận \* Update product.type = combo \*
variant.type = true =\> phiên bản đã trở thành combo sẽ phải bán, trừ
kho ghi nhận theo các thông tin thành phần

3. Update combo gắn với phiên bản combo Điều kiện: \* Đã có sản phẩm +
phiên bản combo Method: PUT a. Input Thông tin hệ thống Validate
required? Input Note Parent {} parent_product_id Big integer No ID sản
phẩm combo chứa các sản phẩm thành phần

parent_variant_id string No ID phiên bản combo chứa các sản phẩm thành
phần

calculate_type enum Yes Cách tính giá của sản phẩm combo combo_sum: giá
phiên bản combo = Σ(giá combo_variant x số lượng trong combo) Fixed: giá
cố định do user tự truyền None: giá của phiên bản combo sẽ không được
điều chỉnh price decimal No Giá sản phẩm combo Max: 999,999,999 Min: 0
combo \[\] combo_varant_id Big integer Yes ID phiên bản thành phần

quantity interger\[d\] Yes Số lượng sản phẩm thành phần. Lớn hơn 0

b. Output \* Hệ thống tự tính toán giá của phiên bản combo và ghi nhận
vào variant.price = giá ghi nhận =\> Không truyền -\> Không ghi nhận \*
Hệ thống update lại kho + giá vốn cho phiên bản combo  1. Xóa thành phần
trong combo Điều kiện: \* Đã có sản phẩm + phiên bản combo \* Thực hiện
xóa thành phần trong combo Method: DELETE a. Input Thông tin hệ thống
Validate required? Input Note Parent {} parent_product_id Big integer No
ID sản phẩm combo chứa các sản phẩm thành phần

parent_variant_id string Yes ID phiên bản combo chứa các sản phẩm thành
phần

combo \[\] combo_varant_id Big integer Yes ID phiên bản thành phần

b. Output \* Nếu xóa toàn bộ combo_variant của 1 parent_variant =\> Hệ
thống update product.type = normal và variant.type = true =\> Kho ghi
nhận bằng inventory_level đang lưu trong hệ thống \* Nếu còn ít nhất 1
combo_variant của 1 parent_variant =\> Hệ thống ghi nhận xóa 1 thành
phần của combo \* Báo lỗi trong trường hợp combo_variant_id không tìm
thấy \* Combo service xử lý update thông tin combo  1. Xóa phiên bản sản
phẩm tác động đến combo 1. Phiên bản là thành phần combo Input: Xóa
phiên bản là combo thành phần Output: Xóa combo_item có combo_variant_id
= variant bị xóa 2. Xóa phiên bản là phiên bản cha Input: Xóa phiên bản
là parent_variant Output: Xóa tất cả combo_item có parent_variant_id =
variant bị xóa 2. Thông tin kho với sản phẩm combo 1. User story \* US1:
Là chủ cửa hàng, tôi MUỐN khi search sản phẩm combo và có trả về số
lượng combo hiện có trên toàn bộ cửa hàng, nhờ vậy tôi có thể thông báo
cho người mua về số lượng có thể bán \* US2: Là các client, tôi MUỐN sử
dụng thông tin kho combo (order/draft order/checkout/cart) để thực hiện
nghiệp vụ thêm sản phẩm vào đơn \* US3: Là admin user, tôi MUỐN xem
thông tin kho + số lượng tồn kho ảo của sản phẩm combo được hiển thị
trong danh sách sản phẩm để bổ sung tồn kho thành phần khi hết hàng \*
US4: Là các kênh bán hàng (POS, SOCIAL), tôi MUỐN lấy thông tin kho + số
lượng tồn kho để hiển thị trên kênh bán hàng của mình 2. Thông tin kho
của combo Trong các combo_item của combo: chỉ cần tồn tại ít nhất 1
combo_item có trường sẽ ảnh hưởng tới thông tin combo cha Thông tin
combo_item TH đặc biệt inventory_management Sapo

required_shipping true

inventory_policy deny

Bảng test scenarios Ký hiệu: p: thông tin resource product parent trong
combo c: thông tin resource product combo_item trong combo Scenarios
Input Output

p c p p.product_listing p.webhook Create Combo

Thông tin p khác ít nhất 1 c

inventory_management = null inventory_quantity = 0 required_shipping =
false inventory_policy = cont inventory_management = Sapo
inventory_quantity = const required_shipping = true inventory_policy =
deny inventory_management = Sapo inventory_quantity = c.const.ratio
required_shipping = true inventory_policy = deny inventory_management =
Sapo inventory_quantity= c.const.ratio required_shipping = true
inventory_policy = deny inventory_management = Sapo inventory_quantity =
c.const.ratio required_shipping = true inventory_policy = deny Update
Combo Update thông tin kho của các c giống nhau inventory_management =
null inventory_quantity = 0 required_shipping = false\[e\]
inventory_policy = deny inventory_management = Sapo inventory_quantity =
const required_shipping = true inventory_policy = cont
inventory_management = Sapo inventory_quantity = c.const.ratio
required_shipping = true inventory_policy = deny inventory_management =
Sapo inventory_quantity= c.const.ratio required_shipping = true
inventory_policy = deny inventory_management = Sapo inventory_quantity =
c.const.ratio required_shipping = true inventory_policy = deny Update
thông tin kho của các c khác nhau inventory_management = Sapo
inventory_quantity = 0 required_shipping = false inventory_policy = deny
inventory_management = Null inventory_quantity = const required_shipping
= true inventory_policy = cont inventory_management = Null
inventory_quantity = c.const.ratio required_shipping = true
inventory_policy = cont inventory_management = Null inventory_quantity =
c.const.ratio required_shipping = true inventory_policy = cont
inventory_management = Null inventory_quantity = c.const.ratio
required_shipping = true inventory_policy = cont Delete Combo Xóa tất cả
sản phẩm trong combo

inventory policy = deny inventory_quantity = 0 inventory_management=
null requires_shipping = true

Delete = 0 3. Số lượng tồn kho của combo \* Có trường tổng hợp thông tin
số lượng tồn kho để trả ra trong response phiên bản sản phẩm \* Công
thức tồn kho của phiên bản combo tính theo phiên bản thành phần: Ghi
chú: - Combo cha: \* Thành phần combo: , ,.., Tổng số tồn kho của thành
phần combo trên hệ thống = : , ,\..., =\> Số lượng tồn kho của thành
phần combo (lấy phần nguyên): = =\> Số lượng của sản phẩm combo là tỷ lệ
số tồn kho nhỏ nhất = min( , , ..., )

7. Xuất nhập file sản phẩm combo File mẫu AC1: Tạo mới sản phẩm combo
với tên sản phẩm và phiên bản thành phần trong file AC2: Cập nhật thành
phần sản phẩm combo trong trường hợp trúng alias của sản phẩm combo đã
tồn tại trên hệ thống AC3: Line đầu tiên của sản phẩm combo là thông tin
combo, chỉ ghi nhận những thông tin sau: \* Alias và tên sản phẩm, nếu
không có alias, hệ thống tự sinh alias để khởi tạo sản phẩm \* Giá combo
\* Giá combo rỗng -\> hệ thống tính giá dựa trên tỉ lệ thành phần \* Giá
combo = const -\> hệ thống ghi nhận giá sản phẩm = const AC4: Check
trùng phiên bản thành phần theo alias sản phẩm + thuộc tính + giá trị
thuộc tính AC5: Trường hợp user xóa dòng đầu tiên -\> Hệ thống báo lỗi
và không cập nhật/tạo sản phẩm đó AC6: Trường hợp có nhiều phiên bản
trùng nhau trong file -\> Hệ thống chỉ ghi nhận dòng phiên bản đầu tiên
và ignore các dòng còn lại AC7: Trường hợp không tìm được phiên bản gốc
-\> báo lỗi AC8: Hiện tại do chưa hỗ trợ luồng quản lý variant combo
trên giao diện nên chưa hỗ trợ nhập file combo theo phiên bản AC9: Các
usecase báo lỗi Usecase Lỗi Unit trong phiên bản bị trùng STT dòng: Đã
tồn tại đơn vị quy đổi \"\...\" cho phiên bản này Thông tin phiên bản
sai alias STT dòng:Alias của phiên bản không chính xác Thiếu thông tin
số lượng thành phần combo STT dòng: Sản phẩm thành phần \"\...\" không
có thông tin số lượng User điều chỉnh tỉ lệ của đơn vị quy đổi Bỏ qua
cập nhật tỉ lệ

AC10: Check quyền xuất nhập file theo quyền xuất file sản phẩm AC11:
Check quyền nhập file nếu user có quyền Tạo hoặc Cập nhật sản phẩm sẽ
hiển thị button, logic API nhập check theo Phần 8. Phân quyền tạo sản
phẩm Combo

8. Phân quyền tạo sản phẩm Combo  1. API liên quan a. API combo Lý do xử
lý phân quyền cho API combo: API combo bị ảnh hưởng do khi tạo combo sẽ
update loại sản phẩm normal -\> combo Mô tả: \* Sản phẩm không phân
quyền theo chi nhánh -\> Nhìn được tổng số lượng sản phẩm combo trên
tổng tất cả kho \* Khi user không có quyền read products, thời điểm
create products vẫn có thể tạo được combo khi có variant ids GET read
products read cost price create products update products update cost
price delete products export products /admin/combos v

/admin/combos/count v

/admin/combos/{variant_id} v

POST

/admin/combos

v

/admin/combos/{variant_id}/combo_items

v

PUT

/admin/combos/{variant_id}

v

DELETE

/admin/combos/{variant_id}

v

/admin/combos/{variant_id}/combo_items/{combo_item_id}

v

b\. API sản phẩm + phiên bản API sản phẩm + phiên bản được check trong
trải nghiệm tạo sản phẩm combo: Create Product + Variant -\> Create
combo =\> Check quyền khi user trải nghiệm khởi tạo/xem chi tiết sản
phẩm/ danh sách sản phẩm theo phân quyền product + variant c. API Kho
Sản phẩm combo không sử dụng tới kho thực tế =\> Trải nghiệm không bị
ảnh hưởng

2. FE giao diện phân quyền

Product - inventory Danh sách sản phẩm Thêm mới sản phẩm Chi tiết sản
phẩm Chi tiết phiên bản Thông tin kho Quản lý kho Không có quyền xem sản
phẩm  - Không xem được danh sách - Truy cập báo không có quyền  - Không
thêm mới được sản phẩm - Truy cập báo không có quyền  - Truy cập báo
không có quyền  - Truy cập báo không có quyền

Không có quyền sửa sản phẩm  - Ẩn bulk action sửa sản phẩm - Ẩn nút thêm
mới sản phẩm combo

 - Không được sửa bất cứ trường gì - Không vào được màn tạo sp combo

Không có quyền tạo sản phẩm Ẩn nút thêm mới sản phẩm combo  - Truy cập
báo không có quyền

Không có quyền xem giá vốn

 - Không set giá vốn (mặc định = 0)  - Không hiển thị giá vốn  - Không
hiển thị giá vốn

Không có quyền sửa giá vốn

 - Không set giá vốn (mặc định = 0)  - Không sửa giá vốn  - Không sửa
giá vốn

Không có quyền xoá sản phẩm  - Ẩn bulk action xoá sản phẩm

Ẩn nút xoá sản phẩm và chỉnh sửa xoá phiên bản Ẩn nút xóa

Không có quyền xem tồn kho  - Không có quyền ờ chi nhánh nào: Ẩn thông
tin Có thể bán - Hiển thị tổng tồn kho các chi nhánh có quyền xem (sp
thường, combo, packsize)

 - Không hiển thị các chỉ số kho ở chi nhánh ko có quyền (sp thường,
combo, packsize)  - Không hiển thị các chỉ số kho ở chi nhánh ko có
quyền - Ẩn link xem lịch sử kho (nếu ko có quyền xem tồn kho ở tất cả
chi nhánh). Nếu có quyền ở ít nhất 1 chi nhánh thì hiển thị link

9. Tạo Đơn hàng/Checkout với combo  1. Các vấn đề \* Kênh bán hàng muốn
hỗ trợ bán các sản phẩm combo thông qua checkout \* Trong admin, cho
phép user tạo đơn đơn hàng cho sản phẩm combo  1. Định hướng \* Lineitem
là các variant thành phần (combo_items.variant_id) \* Giá trong lineitem
là giá đã chia ra tỉ lệ từ combo \* Số lượng của từng line item =
quantity combo item\* số lượng combo \* Order trừ kho theo lineitem ghi
nhận trong đơn \* Order bổ sung 1 thông tin capture sản phẩm combo gốc
 1. Tạo đơn hàng với combo

Mô hình quan hệ lineitem order - sản phẩm combo

Thông tin line_item_group Thông tin Validate required? Input Note id Big
integer Yes ID nhóm sản phẩm(combo) được capture trong order

line_item_ids

Yes Danh sách các line_item thuộc line_item_groups

variant_id Big integer Yes ID phiên bản sản phẩm combo

quantity Number Yes Số lượng combo được mua trong đơn

title String Yes Tên sản phẩm combo

Ghi nhận combo vào Order

2. Tạo checkout với combo

Mô hình quan hệ lineitem Checkout - sản phẩm combo

Thông tin componentizable_line_item Thông tin Validate required? Input
Note variant_id Big integer Yes ID line item được capture trong checkout
(của sản phẩm combo)

quantity Number Yes Số lượng combo được mua trong đơn

title String Yes Tên sản phẩm combo

line_components Object Yes Các sản phẩm thành phần của combo

varaint_id

Yes combo_item.variant_id

quantity

Yes Số lượng sản phẩm thành phần trong đơn

title

Yes Tên sản phẩm thành phần

Ghi nhận combo vào Checkout

3. Ghi nhận giá trị combo trong order/checkout Phạm vi Mô tả Admin
Orders Order.Line_item Giá ghi nhận \* Giá tổng là giá ghi nhận theo
phiên bản cha. Sau đó khi ghi nhận lineitem vào đơn sẽ được phân bổ cho
từng phiên bản thành phần dựa trên trọng số giá gốc của phiên bản \* Nếu
tất cả combo variant có giá = 0 =\> Phân bổ giá cho lineitem đầu tiên
trong danh sách combo_items \* Nếu có ít nhất 1 combo variant có giá
khác 0 =\> Công thức tính giá phân bổ như sau: P(C) = x\*sum(P(i)xQ(i))
= sum(P\'(i) x Q\'(i)) Số lượng ghi nhận: \* Là số lượng theo cấp số
nhân trong bảng combo \* Line_item.quantity = combo_item.quantity x số
lượng combo trong đơn Line_item_group: \* id: ID nhóm sản phẩm(combo)
được capture trong order \* Variant_id: id phiên bản của combo cha \*
quantity: Số lượng combo được mua trong đơn \* title: Tên sản phẩm combo
Discounts Discount tính trên phiên bản cha và phân bổ xuống các phiên
bản thành phần Sản phẩm cha phải thỏa mãn Chương trình khuyến mãi/ Mã
khuyến mãi mới có thể áp dụng Taxes Thuế tính trên phiên bản thành phần
Áp dụng trên giá trị lineitem sau khi được phân bổ từ giá combo cha
Fulfill đơn Fulfill đơn theo variant con Refund/Returns Hoàn Trả theo
variant con Reports Sales report theo variant con Checkout Checkout và
cart Đảm bảo không cho phép bán vượt mức cho phép số lượng tồn kho của
sản phẩm cha = quantity nhỏ nhất của variant con chia ra Check routing
sản phẩm trên checkout theo sản phẩm combo Giá ghi nhận \* Giá tổng là
giá ghi nhận theo phiên bản cha. Sau đó khi ghi nhận lineitem vào đơn sẽ
được phân bổ cho từng phiên bản thành phần dựa trên trọng số giá gốc của
phiên bản \* Nếu tất cả combo variant có giá = 0 =\> Phân bổ giá cho
lineitem đầu tiên trong danh sách combo_items \* Nếu có ít nhất 1 combo
variant có giá khác 0 =\> Công thức tính giá phân bổ như sau: P(C) =
x\*sum(P(i)xQ(i)) = sum(P\'(i) x Q\'(i)) Số lượng ghi nhận: \* Là số
lượng theo cấp số nhân trong bảng combo \* line_components.quantity =
combo_item.quantity x số lượng combo trong checkout line_components: \*
id: ID sản phẩm thành phần được capture trong checkout \* Variant_id: id
phiên bản của combo item - combo con \* quantity: Số lượng thành phần
combo được mua trong đơn \* title: Tên sản phẩm thành phần

10. Báo cáo  1. Báo cáo tồn kho Không có quản lý kho theo sản phẩm combo
mà trừ đi các sản phẩm thành phần trong kho 2. Báo cáo bán hàng Ghi nhận
báo cáo theo thành phần combo \* Variant id thành phần combo \* Product
id thành phần Vấn đề Giải quyết Xem báo cáo bán hàng có chứa các sản
phẩm thành phần bên trong v Điều chỉnh sản phẩm trong combo \* Ghi nhận
báo cáo bán hàng \* Ghi nhận báo cáo tồn kho \* Hoàn hàng + trả hàng v
Ghi nhận báo cáo bán hàng: theo sản phẩm gốc Lịch sử tồn kho thay đổi
theo lineitem ghi nhận trong sản phẩm thành phần gắn với combo tại thời
điểm tạo đơn Hoàn trả hàng sẽ update lại kho theo sản phẩm thành phần
Báo cáo theo thành phần trong combo VD: Mua 1 combo (2 sản phẩm A, B) và
5 sản phẩm A =\> báo cáo tính thành 7 sản phẩm A và 1 sản phẩm B v

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

11. Mô tả giao diện  1. Thêm mới sản phẩm combo POST /admin/combos

Flow FE:

Ghi nhận thông tin resource Product

Trường thông tin API Mô tả Product Tên sản phẩm product.title Thông tin
tên sản phẩm Mã SKU product.sku SKU không bắt buộc Mã vạch barcode
product.barcode Barcode không bắt buộc Ảnh product.images

Kênh bán hàng Resource_publication\[ \]

Thông tin seo meta_description meta_title

Danh mục Collections \[\]

Nhà sản xuất product.vendor

Loại sản phẩm product.product_type

Tags product.tag

Variant Giá bán variants.price Giao diện gọi ý giá theo tổng giá các sản
phẩm thành phần trong combo

Giá gợi ý =

Pi: Giá sản phẩm thành phần Qi: số lượng sản phẩm thành phần trong combo
Giá so sánh variants.compate_at_price

Áp dụng thuế variants.taxable

Sản phẩm yêu cầu vận chuyển variants.requires_shipping

Khối lượng variants.weight

Đơn vị khối lượng variants.weight_unit

Quản lý kho variants.inventory_management mặc định inventory_management
= null

Ghi nhận thông tin resource Combo

Thông tin hiển thị Trường trong API Mô tả Thông tin sản phẩm thành
phần - combo_items

\"combo_items\": \[ { \"variant_id\": 0, \"quantity\": 0 } \] Tên sản
phẩm product.title Thông tin tên sản phẩm Tên phiên bản product.option

Mã SKU product.sku SKU không bắt buộc Mã vạch barcode product.barcode
Barcode không bắt buộc Ảnh product.images

Id phiên bản variant.id combo_items.variant_id Id phiên bản thành phần
Dùng cho combo_items.variant_id Số lượng combo_items.quantity Số lượng
sản phẩm trong combo Điều kiện: Integer Min = 1 Max = 999,999,999 Giá
bán variant.price Giá bán của phiên bản Giá vốn
variant.inventory_item.cost_price Giá vốn của phiên bản Thông tin combo
cha Giá so sánh variant.compare_at_price Không tự động gợi ý giá Giá vốn
variant.inventory_item.cost_price

Gợi ý giá vốn = Pi = giá vốn thành phần Giá gốc combo.price Giá gợi ý =

Pi: Giá sản phẩm thành phần Qi: số lượng sản phẩm thành phần trong combo

Truyền vào trường combo.price Trường hợp tổng giá thành phần \> max
999,999,999 =\> báo lỗi "giá lớn hơn 999,999,999"

2. Chỉnh sản phẩm combo Chỉnh sửa thành phần combo Scenario Giao diện
Input Output Chỉnh sửa số lượng các combo_items đang có Khi nhập đổi số
lượng combo item =\> giá bán và giá vốn dự kiến update tương ứng

Giá bán sản phẩm không tự động đổi

User ấn Lưu -\> Gọi API PUT /admin/combos/{variant_id} { \"combo\": {
\"variant_id\": {id phiên bản combo}, \"combo_items\": \[ {
\"variant_id\": {id phiên bản thành phần đã sửa}, \"quantity\": 0 } \],
\"price\": {} } } Update số lượng combo_item Update giá sản phẩm nếu
truyền giá (Dùng API product) Thêm mới combo_items vào combo đang có
User chọn từ thanh tìm kiếm combo mới -\> Chọn phiên bản -\> điền số
lượng =\> giá bán và giá vốn dự kiến update tương ứng

Giá bán sản phẩm không tự động đổi

User ấn Lưu -\> Gọi API PUT /admin/combos/{variant_id} { \"combo\": {
\"variant_id\": {id phiên bản combo}, \"combo_items\": \[ {
\"variant_id\": {id phiên bản thành phần đã sửa}, \"quantity\": 0 } \],
\"price\": {} } } Update số lượng combo_item Update giá sản phẩm nếu
truyền giá (Dùng API product) Xóa combo_items User chọn bỏ xóa
combo_items =\> Lưu =\> Hiển thị popup confirm

=\>Xóa =\> Gọi API DELETE
/admin/combos/{variant_id}/combo_items/{combo_item_id}

\"variant_id\": {id phiên bản combo} "Combo_item_id": {id phiên bản
thành phần đã sửa} Xóa thành phần sản phẩm combo

Chỉnh sửa thông tin combo Chỉnh sửa thông tin combo như sản phẩm thường,
sử dụng API product \[a\]Bổ sung nghiệp vụ \[b\]Mặc định không truyền
giá = tổng component \[c\]Case giao diện không muốn truyền thêm giá để
giữ nguyên giá sẽ xử lý như thế nào? \[d\]@loanvtp@sapo.vn \_Assigned to
loanvtp@sapo.vn\_ \[e\]Không update thông tin required_shipping sản phẩm
gốc =\> ko update sản phẩm combo \@manhnd4@sapo.vn \@loanvtp@sapo.vn
\_Assigned to manhnd4@sapo.vn\_
