# 1 số hàm dùng cho chuỗi
strc = strB in strA #ktra xem chuỗi B có phải chuỗi con của A ko
x = len(a) độ dài của chuỗi a gán cho x
a = strA[x:y] cắt chuỗi con A từ vị trí x -> y
b = strA[x:y:z] chuỗi chuỗi x->y với khoảng cách z
với z = -1 thì chuỗi chuỗi theo chiều ngược lại
s = "nam sinh của tôi là %s %s %d..." %("1","2","3")
        gán lần lượt các giá trị theo thứ tự vào chuỗi
        %s là gán kí tự
        %d là số nguyên or số thực
        
# 1 số hàm quen thuộc trong thư viện math
from math import *
a = sprt(a)
a = isqrt(a) hàm trả về phần nguyên của căn bậc 2
a = pow(5,2) 5 lũy thừa 2
a = ceil(a) làm tròn lên
a = floor(a) làm tròn xuống
a = factorial(a) tính giai thừa của a
a = gcd(a,b) ước chung lớn nhất của a và b
a = comb(n, k) tổ hợp chập k của n
a = fabs(a) trị tuyệt đối
a = max(a,b,c,d)
a = min(a,b,c,d)
a = sum([1,2,3,4,5])
check = "true" if a < b else 'false' 
nếu a < b thì trả về true và ngược lại ( trả về giá trị cho biến check)
# list trong python
khai báo là []
a = a.append([a,b,c]) thêm 1 list mới vào list ban đầu
a = a.extend([a,b,c]) thêm từng phần từ mới vào list ban đầu
a = a.insert(x,1) thêm 1 vào vị trí x
c = a.pop(1) gán gtri của a[1] cho c và loại bỏ a[1] ra khỏi list
a = a.remove(x) loại bỏ 1 lần giá trị x ra khỏi list
a = a.reverse() đảo ngược list
a = a.sort() sắp xếp tăng dần
a = a.sorted() sắp xếp tạm thời 1 lần mà không ảnh hưởng thứ tự gốc
a = a.sort(reverse = True) sắp xếp giảm dần
a = b.copy() sao chép b cho a nhưng ko khác địa chỉ
del a[2] xóa phần tử a[2] ra khỏi list

# kiểu tuple trong Python
khai báo là ()
a = (1,2,3,4) or a = tuple(1,2,3,4)




# 1 số hàm dùng trong NUMPY
import numpy as np
a = np.array([1,2,3]) tạo mảng 1 chiều
c = a.shape   kiểm tra ma trận có bao nhiêu hàng vs cột
a = np.array([[1,2,3],[4,5,6]]) tạo mảng 2 chiều
a = np.diag([1,2,3]) tạo ma trận đường chéo chính
a = np.arange(x) tạo ma trận 1 chiều từ 0 -> x-1
a = np.zeros((2,2)) tạo mảng 2x2 toàn 0
a = np.ones((1,2)) tạo mảng 1x2 toàn 1
a = np.full((3,2,2),x) tạo mảng 3x2x2 toàn x
a = np.eye(3) tạo ma trận đơn vị 3x3
a = np.random.rand(3,2) tạo ma trận 3x2 ngẫu nhiên
a = np.array([[1,2,3],[4,5,6]], np.int32) tạo mảng với kiểu int32
print(a.ndim) in ra số chiều trong mảng
print(a.size) in ra tổng số phần tử trong mảng
a.dtype in ra kiểu của mảng
a = np.arange(x).reshape(a,b,c) tạo mảng có giá trị từ 0 -> x-1
b = a.reshape(x,-1) chỉnh cỡ ma trận thì x dòng và n/x cột
có nhiều chiều thành a,b,c............
# 1 số hàm numpy về ma trận
                a = np.array([[1,2,3],[4,5,6]])
                b = np.array([[1,2,3],[4,5,6]])
        c = a+b = np.add(a,b)
        c = a*b = np.multiply(a,b)
        c = a-b = np.subtract(a,b)
        c = a/b = np.divide(a,b)
        c = np.sprt(a) khai căn tất cả phần tử trong a
        c = 2**x tính 2 mũ tất cả các phần tử trong x
// nhân ma trận => c = a.dot(b) = np.dot(a,b)
// c = np.linalg.inv(x) ma trận nghịch đảo của x
// c = a.T   => ma trậm chuyển vị của a
// c = np.sum(a) tính tổng của ma trận
// c = np.sum(a , axis = 0) in mảng 1 chiều với giá trị là tổng cột của ma trận
// c = np.sum(a , axis = 1) tổng hàng của ma trần
// a[np.arange(x),b] tính theo chỉ số 
ví dụ với x = 4 và b là [1,3,3,2] thì có các chỉ số là
        a[0,1], a[1,3], a[2,3], a[3,2]
// với biến bool_x = a > 2
        print(bool_x) in ra mảng true false
        print(a[check]) in ra các giá trị thỏa mãn đkien
// np.log(x) lấy log cơ số e của từng phần tử
// np.abs(x) lấy trị tuyệt đối
// np.maximum(x,2) số sánh từng phần tử của x với 2 và gán lại max cho vị trí đó
// np.max(x) tìm giá trị lớn nhất của x
// np.max(x ,axis=0) tìm giá trị lớn nhất của mỗi cột
// np.max(x ,axis=1) tìm giá trị lớn nhất của mỗi hàng
// x**2 => lũy thừa 2 của từng phần tử




# 1 số hàm trong Pandas
import pandas as pd
// datafrachi_so = ["x","y","z"] x,y,z là tên các hàng
        gia_tri = [310,323,233]
        a = pd.Series(gia_tri,index= chi_so)me = pd.read_csv("tên flie",sep = ",",header = None, name =[??,??,??])
        với sep là cách phân biệt các cột
            header là tên cột
            name   là đặt lại tên cột nếu ko có tên cột
// có thể gọi hàm chỉ với câu lệnh
        dataframe = pd.read_csv("ten file") hoặc đường dẫn file
        //chú ý csv là đuôi của file csv or txt
        gọi read_excel nếu đọc file excel
        pd.read_excel("tên file",sheet_name="xxx",header=None,name=[???])
//data1 = data.sort_values([name])
        sắp xếp data theo dữ liệu cần sắp xếp
//data1 = data.query('name=="???"')
        lọc dữ liệu theo trường cần lọc



# dùng cả NUMPY và PANDAS
// a = pd.Series(np.random.randint(100,size=x))
khởi tạo x hàng mỗi có giá trị ngẫu nhiên < 100
        print(a.index, a.values)
// khởi tạo mảng gán giá trị theo chỉ số
         
        print(a["x"],a["y"],a["z"]) truy vấn dữ liệu
        hoặc là truy vấn bằng a.x, a.y, a.z

// có 2 Series A và B thì
        A+B sẽ cộng các "name" giống nhau còn ko có sẽ in ra NaN
// một số hàm trong Series
        print(a.ndim) trả về số chiều của a
        print(a.values) trả về các phần tử của a
        print(a.head(n)) trả về n phần tử đầu tiên 
        print(a.tail(n)) trả về n phần tử cuối cùng
        print(a.axes) trả về danh sách các chỉ số của a
        print(a.dtype) các kiểu dữ liệu
        print(a.empty) trả về True nếu a rỗng
        print(a.size) trả về số phần tử của a

// tạo hàm def và dùng hàm apply không khiến thay đổi giá trị của a
        ví dụ def tăng_gia_trị
               print(a.apply(tăng_gia_tri))
// LÀM VIỆC VỚI DATA_FRAME
a = pd.DataFrame(data, index, columns, dtype, copy)
        data nhận dữ liệu từ nhiều kiểu khác nhau
        index là chỉ mục hàng
        columns là chỉ mục cột
        dtype kiểu dữ liệu mỗi cột
        copy có lưu đè hay không // mặc định là False 


//LÀM VIỆC VỚI SET
my_set = {4, 2, 3} # my_set = set([1, 2, 3])