C:\\Users\\Sapoer\\Downloads\\Screenshot - 2020-02-01T105026.376.png

PHÂN TÍCH YÊU CẦU Quản lý Catalog - Bảng giá

Tháng 1, 2023 \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ MỤC LỤC 1. Mục đích 3 2.
Phạm vi ảnh hưởng 3 3. Khái niệm, định nghĩa 3 4. Tài liệu liên quan 3
5. Tổng quan mô hình sản phẩm 4 6. Chi tiết tính năng 5 6.1. Quản lý
Điều kiện áp dụng chính sách giá 5 6.1.1. Luồng tổng quan 5 6.1.2. Quản
lý Điều kiện áp dụng - Catalog 6 a. Khởi tạo Điều kiện áp dụng 6 b.
Chỉnh sửa thông tin Điều kiện áp dụng 7 c. Xóa Điều kiện áp dụng 8 d.
Lấy danh sách điều kiện áp dụng 8 e. Lấy một điều kiện áp dụng cụ thể 8
6.1.3. Quản lý chính sách giá - Pricelist 9 a. Khởi tạo chính sách giá 9
b. Update chính sách giá 10 c. Xóa chính sách giá 11 6.1.4. Quản lý giá
chính sách - PricelistPrice 11 a. Khởi tạo giá chính sách 11 b. Update
giá chính sách 11 c. Xóa giá chính sách 12 6.1.5. Thiết lập điều kiện áp
dụng chính sách giá - Customer Group/App/Location 12 6.1.6. Hiển thị
Điều kiện áp dụng theo đối tượng - Publication 12 6.2. Trả về thông tin
chính sách giá với điều kiện áp dụng tương ứng 13 6.2.1. Các usecase
liên quan 13 6.2.2. Luồng nghiệp vụ tổng quan 13

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

1\. Mục đích \* Trong quá trình bán hàng, chủ cửa hàng mong muốn quản lý
chính sách giá với các mục đích: \* Thiết lập giá trong đơn hàng theo
các logic mong muốn: áp dụng cho nhóm khách hàng nào, kênh bán hàng nào,
chi nhánh nào \* Nhân viên không thể gian lận đổi giá sản phẩm sẽ không
được phép 2. Phạm vi ảnh hưởng \* Module sản phẩm \* Module Đơn hàng \*
Checkout \* Storefront 3. Khái niệm, định nghĩa STT Ký tự Diễn giải 1 KH
Khách hàng: chủ cửa hàng, nhân viên, các đối tượng sử dụng phần mềm để
thực hiện các công việc 2 SP Sản phẩm

4\. Updated version

Version Ngày cập nhật Mô tả V1.0 05/2024 Mô tả nghiệp vụ CRUD Catalog
V1.1 06/2024 Bổ sung nghiệp vụ Product áp dụng Catalog (chi tiết) V1.3
24/07/2024 Điều chỉnh nghiệp vụ: Tách Variant dùng cho pricelist và
product trong publication của Catalog

5\. Tài liệu liên quan STT Tên tài liệu Link 1 Wireframe
https://www.figma.com/design/JrXGet7xnGRdSmXJXSHuBC/Price-list?node-id=0-1&t=yNRADPhEpI1zFkY3-1
2 API http://192.168.81.135:31006/?urls.primaryName=product_catalog 3
BFP (Phân rã tính năng)
https://docs.google.com/spreadsheets/d/1nNbg0JUFDkxF_WoYyXOi5iDeM1h1DPqNcZufEOScPHc/edit#gid=0
4 User flow
https://app.diagrams.net/#G1c-9HfbKbTi44mnAp4A-lHhX22MfwddG7#%7B%22pageId%22%3A%22IlQO3pAjEjZTXHwhvmh1%22%7D
5 Phân quyền
https://docs.google.com/spreadsheets/d/1oQM6MeeqnHSpv6jMAj0DRQazAOgDJqEzIwTJE8S37GY/edit?usp=drive_link
6. Tổng quan mô hình sản phẩm

V1.0

v1.2

Mô tả:

Tên đối tượng

Mô tả Publication Danh sách sản phẩm bày bán Danh sách các sản phẩm và
danh mục được hiển thị cho một đối tượng cụ thể (Nhóm khách hàng/Kênh
bán hàng/Chi nhánh) Catalog Bảng giá/Điều kiện áp dụng sản phẩm Bảng
mapping thông tin danh sách các sản phẩm với setting giá đối và giá do
kênh đó áp dụng PriceList Chính sách giá Chính sách giá - Lưu trữ thông
tin tổng hợp của các chính sách giá gắn với các sản phẩm PriceListParent
Quy tắc giá Quy tắc chung áp dụng cho giá sản phẩm PriceListPrices Giá
chính sách Giá áp dụng cho các sản phẩm thuộc catalog

7\. Chi tiết tính năng  1. Quản lý Điều kiện áp dụng chính sách giá Là
chủ cửa hàng, tôi có nhu cầu quản lý các Điều kiện áp dụng sản phẩm đối
với các đối tượng khác nhau  1. Luồng tổng quan Các mối quan hệ trong mô
hình: \* 1 catalog có 0 hoặc 1 pricelist; \* TH catalog không có chính
sách giá xảy ra khi chủ cửa hàng không muốn áp dụng chính sách giá khác
cho đối tượng được áp dụng \* Kênh bán hàng sẽ được tạo mặc định 1
publication và chưa gắn catalog nào \* 1 pricelist luôn có 1
pricelistParent \* 1 pricelist có thể có 0 hoặc nhiều pricelistPrices \*
1 pricelistPrice gắn với 1 phiên bản sản phẩm trong hệ thống (phiên bản
này thuộc sản phầm không liên quan tới sản phẩm hiển thị trên
publication) \* 1 catalog có 0 hoặc 1 publication \* n catalog có thể
được dùng bởi n location/customer group/app Catalog là đối tượng mapping
thông tin chính sách giá với các điều kiện áp dụng chính sách giá
(location/customer Group/app) và hiển thị danh sách sản phẩm
(Publication)

Usecase:

2. Quản lý Điều kiện áp dụng - Catalog Định nghĩa: Catalog là nơi tổng
hợp thông tin về 1 set các sản phẩm hiển thị (Publication) với 1 mức giá
(pricelist) dưới một điều kiện cụ thể (Customer Group/Channel/Location)

Nghiệp vụ:  1. Khởi tạo Điều kiện áp dụng \* Input: POST:
admin/catalogs.json no. field format required? edit? Mô tả 1 id integer
Yes No Id định danh của catalog 2 title string (255) Yes Yes Tiêu đề của
Điều kiện áp dụng 3 context\[\] array No Yes Id các đối tượng áp dụng
chính sách giá Với từng loại chính sách giá chỉ được áp dụng cho đối
tượng tương ứng

\*Lưu ý: Với case catalog type = app context\[id\] phải trùng với
publication_id =\> Nếu không trùng hệ thống sẽ báo lỗi 4 publication_id
integer No Yes Danh sách sản phẩm hiển thị mức giá được cấu hình trong
chính sách giá Nếu không có trường thông tin này, chính sách giá khi
user login sẽ không hiển thị bất cứ sản phẩm nào 5 pricelist_id integer
No Yes Chính sách giá gắn với Điều kiện áp dụng Nếu không có trường
thông tin này, chính sách giá sẽ áp dụng theo giá sản phẩm thông thường
Pricelist có thể = null Chỉ cho phép gắn với price_list khi trường
price_list của catalog đó = null 5 status enum Yes Yes Trạng thái áp
dụng của Điều kiện áp dụng, gồm 2 trạng thái: \* Active: Đang hoạt
động - Điều kiện áp dụng sẽ được áp dụng vào đơn hàng và gửi thông tin
tới các kênh sử dụng \* Draft: Nháp - Điều kiện áp dụng đang chỉnh sửa
và giá sẽ không được áp dụng trong đơn \* Archive: Lưu trữ - Các client
không sử dụng thông tin của các catalog này 6 type enum Yes No Một Điều
kiện áp dụng chỉ được áp dụng cho 1 loại điều kiệu Phân loại điều kiện
áp dụng Điều kiện áp dụng: \* Customer: Điều kiện áp dụng áp dụng theo
nhóm khách hàng =\> context = customer.group_id \* Location: Điều kiện
áp dụng áp dụng theo chi nhánh =\> context = location_id \* App: Điều
kiện áp dụng áp dụng theo ứng dụng thiết lập (bao gồm kênh bán hàng, ứng
dụng có quyền) =\> context= client_id type = app 7 code string No No Mã
code sinh ra tự động để định danh catalog Sinh ra theo cú pháp
CTL{catalog.id} \* Output: Thông tin Điều kiện áp dụng 2. Chỉnh sửa
thông tin Điều kiện áp dụng \* Input: PUT:
admin/catalogs/{catalog_id}.json no. field format required? edit? Mô tả
2 title string (255) Yes Yes

3 context\[\] array No Yes Context bắt buộc phải đúng loại với type ban
đầu của Điều kiện áp dụng 4 publication_id integer No Yes Khi truyền
publication rỗng -\> ghi nhận thành rỗng Không cho phép update
publication_id đã thuộc catalog khác vào catalog đích Lí do: Nếu cho
phép như vậy catalog chi nhánh có thể lấy publication_id của kênh để gán
vào catalog của mình 5 pricelist_id integer No Yes Mỗi catalogs chỉ có
tối đa 1 chính sách giá 5 status enum Yes Yes

3. Xóa Điều kiện áp dụng Khi xóa Điều kiện áp dụng =\> các đối tượng gắn
với Điều kiện áp dụng vẫn tồn tại =\> Thông tin giá contextPrice trong
sản phẩm trả về thông tin giá ban đầu của sản phẩm
deleteDependentResources (boolean) \* true: xóa hết tất cả pricelist và
publication gắn với catalog này \* false: chỉ xóa catalog Không truyền
mặc định = false Xóa catalog kênh chỉ được phép deleteDependentResources
= false -\> không xóa publication

4\. Lấy danh sách điều kiện áp dụng Input: GET: admin/catalogs.json
Param: limit integer Return up to this many results per page(default:
50)(maximum: 250) page integer Default value : 1 type enum
customer/location/app sortkey

id/title reverse boolean

query

Hỗ trợ lọc theo một trong các điều kiện sau: Title\[a\] hoặc code
publication_id integer Lọc theo publication id áp dụng trong catalog
customer_group_id integer Lọc theo nhóm khách hàng catalog_ids integer
Get nhiều catalogs status enum active/draft/archive Output: Danh sách
Thông tin Điều kiện áp dụng, mặc định trả về theo thứ tự id giảm dần 5.
Lấy một điều kiện áp dụng cụ thể Input: GET: admin/catalogs/{id}.json
Output: Thông tin Điều kiện áp dụng no. field format Mô tả 1 id integer

2 title string (255)

3 context\[\] array \* Trả về list location/app/customer_save_search 4
publication_id integer

5 pricelist_id\[b\] integer

5 status enum \* 6 type enum

7 code string

\*

3. Quản lý chính sách giá - Pricelist Định nghĩa: là đối tượng quản lý
thông tin giá nào gắn với sản phẩm nào trong điều kiện thỏa mãn (thỏa
mãn điều kiện lưu trong catalog)

Nghiệp vụ:  1. Khởi tạo chính sách giá \* Input: POST:
admin/pricelists.json\[c\] no. field format required? edit? Mô tả 1 id
integer Yes No

2 catalog_id integer No Yes Id catalog mà chính sách giá gắn, check điều
kiện áp dụng theo catalog này Một chính sách giá chỉ được gắn với 1
catalog \* Trường hợp catalog đã gắn với 1 pricelist -\> Hệ thống báo
lỗi Catalog đã gắn với 1 chính sách giá trên hệ thống \* Chỉ hỗ trợ gắn
catalog id chưa gắn với pricelist nào \* Có cho phép đưa catalog id =
null 3 currency enum No Yes Tiền tệ áp dụng cho chính sách giá (chưa bắt
buộc cần có trong phase này) 4 title string(255) Yes Yes Tên chính sách
giá Nếu không truyền tên, hệ thống tự động tạo theo cú pháp
{catalog.title} - {unique number} 5 parent object Yes Yes Quy tắc tính
giá trong chính sách 5.1 adjustment object Yes Yes Tỷ lệ áp dụng \*
Type: enum - percentage_increase / percentage_decrease \* Value: decimal
\* Max: 1000 5.2 settings object Yes Yes Cấu hình bổ sung cho chính sách
giá \* CompareAtPriceMode: có áp dụng tỷ lệ áp dụng cho giá so sánh
không \* ADJUSTED: có áp dụng tỷ lệ áp dụng cho giá so sánh - Mặc định
nếu không truyền \* NULLIFY: giá được set = giá ban đầu nếu không được
setup giá cố định \* Output: \* Tạo chính sách giá với các sản phẩm \*
Đồng thời tạo ra các bản ghi PricelistPrice được tính theo tỷ lệ
adjustment với loại type = adjustment \* nếu catalog không gắn với chính
sách giá nào, user sẽ nhìn thấy giá theo product.price và
product.compare_at_price 2. Update chính sách giá Có thể gắn 1 chính
sách giá đã tồn tại với 1 catalog chưa có chính sách giá no. field
format required? edit? Mô tả 2 catalog_id integer No Yes \* Trường hợp
catalog đã gắn với 1 pricelist -\> Hệ thống báo lỗi Catalog đã gắn với 1
chính sách giá trên hệ thống \* Chỉ hỗ trợ gắn catalog id chưa gắn với
pricelist nào 3 currency enum No Yes

4 title string(255) Yes Yes

5 parent object Yes Yes

5.1 adjustment object Yes Yes

5.2 settings object No Yes

\* Output: \* Update thông tin pricelist \* Nếu user update thông tin
adjustment hoặc settings =\> update các pricelistprice có type =
relative theo tỷ lệ adjustment \* Trường hợp catalog đã gắn với 1
pricelist -\> Hệ thống báo lỗi Catalog đã gắn với 1 chính sách giá trên
hệ thống 3. Xóa chính sách giá Khi xóa chính sách giá, các sản phẩm sẽ
được đưa về giá sản phẩm đang có trên hệ thống 4. Quản lý giá chính
sách - PricelistPrice Nghiệp vụ:  1. Khởi tạo giá chính sách \* Input:
POST: admin/pricelistsprice.json no. field format required? edit? Mô tả
1 id integer Yes No

2 price decimal Yes Yes Giá sản phẩm theo chính sách 3 currency enum No
Yes Tiền tệ áp dụng cho chính sách giá 4 compare_at_price decimal Yes
Yes Giá so sánh theo chính sách giá 5 variant_id integer Yes Yes Id
phiên bản sản phẩm gắn với chính sách giá 6 product_id integer No Yes Id
sản phẩm gắn với chính sách giá, sản phẩm không bắt buộc phải thuộc
publication 7 origin_type enum Yes Yes Loại giá chính sách: \* Fixed:
Giá cố định không thay đổi kể cả khi tỷ lệ thay đổi. \* Relative: giá
được tính theo tỷ lệ, chỉ hệ thống admin được tạo tự động loại chính
sách giá này \* Output: \* Tạo giá chính sách giá với các sản phẩm 2.
Update giá chính sách \* Input no. field format required? edit? Mô tả 2
price decimal Yes Yes

3 currency enum No Yes

4 compare_at_price decimal Yes Yes

5 variant_id integer No Yes

6 product_id integer Yes Yes

7 type enum Yes Yes \* \* Output  + Update giá của phiên bản + Hỗ trợ
truyền list phiên bản + giá tối đa 250 id variant 3. Xóa giá chính sách
Sau khi giá cố định bị xóa, giá cho phiên bản sản phẩm bị ảnh hưởng sẽ
tự động được tính bằng cách sử dụng pricelistparent dựa trên tỷ lệ phần
trăm của giá gốc. \* Để xóa giá cố định, cần chỉ định variantId \* Cho
phép xóa tối đa 250 ID variant trong mảng.

5. Thiết lập điều kiện áp dụng chính sách giá -
CustomerGroup/App/Location Sử dụng trường thông tin context trong API
khởi tạo/update chính sách giá để thiết lập đối tượng được sử dụng chính
sách giá Khi các điều kiện trong chính sách giá được thỏa mãn, hệ thống
trả về giá theo sản phẩm tương ứng Thứ tự ưu tiên tính chính sách giá:
Giá theo customer.save_search \> giá theo location \> giá theo kênh 6.
Hiển thị Điều kiện áp dụng theo đối tượng - Publication Định nghĩa:
Publication là nhóm các sản phẩm/danh mục hiển thị cho một catalog
(catalog này có thể hiển thị cho app/chi nhánh/nhóm khách hàng) 1. Điều
kiện hiển thị chính sách giá với nhóm khách hàng Thứ tự ưu tiên hiển
thị: Publication Customer \> Publication của kênh

Publication của Customer Group Publication của kênh KH sử dụng giá 1
publication 1 publication Giá gắn với publication catalog 1 publication
0 publication Giá gắn với publication catalog 0 publication 1
publication Không hiển thị sản phẩm

2\. Điều kiện áp dụng chính sách giá trong đơn hàng admin: ví dụ minh
họa Catalog Product Order 1 pricelist của sản phẩm A: 600k 0 publication
Price sản phẩm: 200k ContextPrice:600k ContextPublish:true ContextPrice:
600k 1 pricelist của sản phẩm A: 600k 1 publication Include sản phẩm
Price sản phẩm: 200k ContextPrice:600k ContextPublish:true ContextPrice:
600k 1 pricelist của sản phẩm A: 600k 1 publication exclude sản phẩm
Price sản phẩm: 200k ContextPrice:200k ContextPublish:false
ContextPrice: 200k

2. Trả về thông tin chính sách giá với điều kiện áp dụng tương ứng  1.
Các usecase liên quan \* Check giá sản phẩm trong một bối cảnh cụ thể \*
Check sản phẩm có hiển thị trong một bối cảnh cụ thể hay không \* Lấy
danh sách các sản phẩm hiển thị trong một bối cảnh cụ thể \* Lấy danh
sách các sản phẩm + giá hiển thị trong một bối cảnh cụ thể  1. Luồng
nghiệp vụ tổng quan 1. Phạm vi ảnh hưởng Danh sách API Resource API
Product GET /admin/products.json GET /admin/products/search.json GET
/admin/products/{id}.json Variant GET /admin/products/{id}/variants.json
GET /admin/variants/{id}.json GET //admin/variants.json

2\. Luồng nghiệp vụ tổng quan

STT Thao tác Đối tượng Mô tả 1 Lấy thông tin giá sản phẩm Client Client
muốn lấy danh sách sản phẩm/phiên bản sản phẩm theo bối cảnh: \* Theo
chi nhánh \* Theo nhóm khách hàng \* Theo kênh bán hàng Input: truyền
điều kiện áp dụng của chính sách sách giá:
location_id/customer.save_search.id / client_id 2 Check thông tin chính
sách giá theo điều kiện ghi nhận trong catalog Product service Gọi API
Check sản phẩm có giá theo điều kiện Hỗ trợ 2 usecase: UC1: Check giá
sản phẩm theo context UC2: Check sản phẩm có hiển thị theo context =\>
Input: customer.save_search/client_id 3 Trả về thông tin chính sách giá
Catalog service Với context tương ứng =\> check catalog gắn với context
=\> pricelist có giá trị nhỏ nhất để trả về =\> Product trả về trong API
thông tin context_price.price và context_price.compare_at_price 4 Trả về
thông tin hiển thị với bối cảnh Catalog service Với context tương ứng
=\> get catalog gắn với context =\> publication_id gắn với context =\>
Product trả về trong thông tin context_publish = true/false

3\. Nghiệp vụ chi tiết Diagram:

Process 1: Điều kiện áp dụng: catalog có status = active

Process 2:

Trường thông tin bổ sung trong API Variants/Products Thông tin Validate
Mô tả Request Bổ sung param \* contextualPricingContext \*
contextualPublicationContext contextualPricingContext

array  - Nếu truyền vào trong API product -\> variant trong response trả
thêm thông tin contextualPricing  - Check giá sản phẩm có giá chính sách
không.  - Nếu không có giá chính sách, giá sản phẩm = giá gốc Request:
Bổ sung param: context(object): cho phép truyền cùng lúc
location_id/customer_save_search_id/publication_id(bắt buộc publication
của app) Vd: contextualPricingContext: { location_id: \"5063573801\",
customer_save_search_id: \"5063573801\", publication_id: \"5063573801\"
}

Bổ sung param: - context_price\_ location_id -
context_price_customer_group_idcustomer_save_search_id\[d\] -
context_price_client_id

contextualPublicationContext array  - Chỉ áp dụng cho API product -
Check sản phẩm có thuộc publication không.  - Nếu không có thuộc
publication trả về = false

Bổ sung param: contextualPublicationContext(object): cho phép truyền
cùng lúc customer_save_search_id/publication_id( publication của app
hoặc của catalog) Vd: contextualPublicationContext: {
customer_save_search_id: \"5063573801\", publication_id: \"5063573801\"
}

Bổ sung param: - context_publication\_ location_id\[e\]\[f\]\[g\] -
context_publication_customer_group_id -
context_publication_publication_id

Response Bổ sung trường thông tin contextualPricing : giá theo chính
sách giá của bảng giá publishedInContext: sản phẩm có hiển thị với điều
kiện của bảng giá hay không contextualPricing object Khi truyền param
contextualPricingContext, response bổ sung đối tượng ContextualPricing
trả thông tin giá theo chính sách giá gồm các thông tin
contextualPricing: \* compareAtPrice \* price \* quantityRule
compareAtPrice float Giá so sánh của sản phẩm, nếu không có giá nằm
trong chính sách giá -\> hệ thống trả về giá so sánh gốc price float Giá
bán của sản phẩm, nếu không có giá nằm trong chính sách giá -\> hệ thống
trả về giá bán gốc quantityRule object Thông tin mua nhiều giá tốt (Làm
sau) publishedInContext boolean Nếu không truyền param
contextualPublicationContext -\> Không trả về trường thông tin này Chỉ
áp dụng cho API product Product gọi vào API check sản phẩm thuộc
publication hay không true: có hiển thị với publication false: không
hiển thị với publication

\[a\]tách ra từng field. Query sẽ filter theo title của catalog \[b\]bỏ
\[c\]chuyển parent và settings ra ngoài { \"price_list\": { \"title\":
\"string\", \"catalog_id\": 0, \"adjustment_value\": 0,
\"adjustment_type\": \"percentage_increase\", \"compare-at_mode\":
\"adjusted\" }

} \[d\]Đổi thành customer_group_id \[e\]@dinhmd@sapo.vn
\@loanvtp@sapo.vn chỗ param publication bỏ của location giúp e/c nhé. Vì
location sẽ check theo tồn kho chứ ko có nhu cầu check theo publication
\_Assigned to dinhmd@sapo.vn\_ \[f\]+1 task phát sinh
\[g\]@maidtn5@sapo.vn done nhé C \@loanvtp@sapo.vn check lại trên
staging giúp e
