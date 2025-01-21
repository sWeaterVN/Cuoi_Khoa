import streamlit as st
st.set_page_config(page_title="C++ basic:D", page_icon=":skull:", layout="centered")

#setup_session_state_variable

#Body
st.title("Tự học C++ từ cơ bản đến nâng cao:D")
lesson=st.selectbox("Chọn khóa học", ["Lập trình cơ bản", "Cấu trúc dữ liệu", "Giải thuật"])

if (lesson=="Lập trình cơ bản"):
    #lesson 1
    st.subheader("I/ Làm quen với C++")
    st.write("1.Khởi tạo một chương trình C++ cơ bản:")
    st.code("""
    #include <bits/stdc++.h>                // Khai báo thư viện 
    using namespace std;
    
    int main() {                            // Khởi tạo hàm chính
        cout << "Hello World!" << endl;     // In ra màn hình dòng chữ Hello World!
        return 0;                           // Return 0 để kết thúc chương trình
    }
    """)
    st.write("Output sau khi chạy mã:")
    output = """
    Hello World!
    """
    st.code(output, language='text')
    st.warning("Trong C++, các câu lệnh kết thúc bằng dấu ';' ")
    st.write("")
    #lesson 2
    st.subheader("II/ Nhập xuất dữ liệu")
    st.write("1.Các kiểu dữ liệu cơ bản trong c++")
    st.code("""
    #include <bits/stdc++.h>               
    using namespace std;
    
    int main() {                            
        int i;              // Khai báo biến i kiểu INTEGER (Kiểu số nguyên)
        float f;            // Khai báo biến f kiểu FLOAT   (Kiểu số thực)
        bool b;             // Khai báo biến b kiểu BOOLEAN (Mang giá trị 0, 1 hoặc true, false)
        string s;           // Khai báo biến s kiểu STRING  (Kiểu xâu kí tự)
        return 0;                          
    }
    """)
    st.write("")

    st.write("2.Nhập xuất dữ liệu")
    output = """
    --------------------------------
    Trong C++ ta nhập / xuất dữ liệu bằng câu lệnh cin và cout
    - Với lệnh nhập, ta dùng cú pháp: cin>>{tên biến};
    - Với lệnh xuất, ta dùng cú pháp: cout<<{biến dữ liệu hoặc thông báo,...};
    --------------------------------
    """

    st.text(output)
    st.code("""
    #include <bits/stdc++.h>               
    using namespace std;
    
    int main() {                            
        int i;          // Khai báo biến i kiểu INTEGER
        cin >> i;       // Nhập giá trị cho i
        
        float f;        // Khai báo biến f kiểu FLOAT
        cin >> f;       // Nhập giá trị cho f


        cout << "Giá trị của i là: " << i;       // Xuất ra màn hình giá trị của i

        cout << "Giá trị của f là: " << f;       // Xuất ra màn hình giá trị của f

        return 0;                          
    }
    """)
    st.write("Output sau khi chạy mã:")
    output = """
    5
    5
    Giá trị của i là: 5 
    Giá trị của f là: 5.0
    """
    st.code(output, language='text')

    #lesson 3
    st.subheader("III/ Làm quen với câu lệnh lặp")
    st.write("1.Lệnh lặp FOR")
    st.code("""
    #include <bits/stdc++.h>               
    using namespace std;
    
    int main() {                            
        cin >> n;
        
        for (int i = 0; i < n; ++i) {   // Vòng lặp for chạy từ 1 đến 10
            cout << i + 1 << " ";
        }

        return 0;                          
    }
    """)
    st.write("Output sau khi chạy mã:")
    output = """
    10
    1 2 3 4 5 6 7 8 9 10
    """
    st.code(output, language='text')
    st.write("")

elif (lesson == "Cấu trúc dữ liệu"):
    #lesson 1
    st.subheader("I/ Cấu trúc dữ liệu Ngăn Xếp (STACK)")
    st.write("1.Khái niệm.\n")
    text = """
    +) Stack là một danh sách được bổ sung 2 thao tác: thêm một phần tử vào cuối danh sách, và loại bỏ một phần tử ở cuối danh sách. Ví trí cuối của Stack được gọi là đỉnh (top).
    
    +) Có thể hình dung Stack như một chồng sách. Việc đặt một quyển sách lên trên cùng chính là thao tác thêm phần tử, và lấy ra quyển sách ở trên đầu là thao tác loại bỏ phần tử. Như vậy, quyển sách được đặt vào sau cùng sẽ luôn được lấy ra trước tiên. Vì tính chất này, Stack còn được gọi là danh sách LIFO (Last In - First Out, hay vào sau - ra trước).
    """
    st.text(text)
    st.image("stack_minh_hoa.png")
    st.write("\nHình ảnh minh họa cho Stack chứa các phần tử kiểu char:")


    st.write("2.Cài đặt.\n")
    st.write("- Cài đặt thủ công.\n")
    st.code("""
    const int MAXN = 1e5 + 2;

    int st[MAXN];
    int top = 0;

    void push(int x) // thêm x vào cuối Stack
    {
        ++top;
        st[top] = x;
    }

    void pop() // loại bỏ phần tử ở cuối Stack
    {
        assert(top); // đảm bảo Stack đang chứa ít nhất 1 phần tử
        --top;
    }

    int peek() // trả về giá trị của phần tử ở đỉnh Stack
    {
        return st[top];
    }
    """)
    text = """
    Thư viện chuẩn của C++ cho phép ta sử dụng Stack qua kiểu dữ liệu stack trong header cùng tên. Các thao tác chính trên stack là:
    +) push: thêm phần tử vào cuối danh sách
    +) top: trả về giá trị phần tử ở cuối danh sách
    +) pop: loại bỏ phần tử ở cuối danh sách

    Ngoài ra, stack cũng hỗ trợ các thao tác:
    +) size: trả về số phần tử hiện có trong stack
    +) empty: trả về trạng thái của stack (true nếu stack rỗng, false nếu stack có ít nhất 1 phần tử)
    """
    st.text(text)
    st.write("\nVí dụ")
    st.code("""
    #include <iostream>
    #include <stack>

    using namespace std;

    int main()
    {
        stack<int> st;
        st.push(5);     // thêm 5 vào stack
        st.push(10);    // thêm 10 vào stack
        cout << st.top() << endl;   // In ra 10
        st.pop();   // loại bỏ phần tử ở cuối
        cout << st.top() << endl;   // In ra 5
        return 0;
    }\n
    """)
    st.image("stack_vi_du.png")
    st.warning("Ngoài ra, ta có thể dùng vector để biểu diễn một Stack. Các hàm push, top và pop sẽ được thay bằng push_back, pop_back và back khi sử dụng vector.")
