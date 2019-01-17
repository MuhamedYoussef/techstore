const items_in_cart = document.getElementById("items_in_cart");
const cart_template = document.getElementById("cart_template");
const cart_modal_template = document.getElementById("cart_modal_template");

let cart = JSON.parse(localStorage.getItem("cart_items")) || [];
items_in_cart.innerHTML = cart.length;
let due_amount = 0;

AddToCart = id => {
  cart.push(id);
  localStorage.setItem("cart_items", JSON.stringify(cart));
  items_in_cart.innerHTML = cart.length;
};

/**** FOR CART PAGE ****/
build_cart_template = products => {
  temp = "";
  products.forEach(product => {
    temp += `
    <div class="row shadow my-3 bg-dark p-3 rounded">
      <div class="col-4">
        <img 
          src="${product.fields.image_url}" 
          class="img-fluid rounded" 
          alt="product photo"
          style="max-width:100px"
        />
      </div>
      <div class="col-7">
        <h6>${product.fields.name}</h6>
        <p>$${product.fields.price}</p>
      </div>
      <div class="col-1">
        <a id="${product.pk}" onclick="remove_item(${product.pk})" >
          <i class="fas fa-times ml-4"></i>
        </a>
      </div>
    </div>`;
  });

  temp += `
    <div class="row shadow my-3 bg-dark p-3 rounded">
      <div class="col-6">
      <h3 class="font-weight-bold text-primary">Total Due Amount</h3>
      </div>
      <div class="col-6">
      <h3 class="font-weight-bold text-primary">$${due_amount}</h3>
      </div>
    </div>`;

  cart_template.innerHTML = temp;
};

/**** FOR MODAL ****/
build_cart_modal_template = products => {
  temp = "";

  products.map((product, index) => {
    temp += `
        <tr>
          <th scope="row">${index + 1}</th>
          <td>${product.fields.name}</td>
          <td>${product.fields.price}$</td>
          <td>
            <a id="${product.pk}" onclick="remove_item(${product.pk})" >
              <i class="fas fa-times ml-4"></i>
            </a>
          </td>
        </tr>
        `;
  });

  temp += `
    <br><br><br><br>
    <tr class="mt-3">
      <th>
        <td class="h4 font-weight-bold text-primary">Total Amount:</td>
        <td class="h4 font-weight-bold text-primary">$${due_amount}</td>
        <td></td>
      </th>
    </tr>
  `;

  cart_modal_template.innerHTML = temp;
};

get_cart_items = () => {
  if (cart.length == 0) {
    try {
      cart_modal_template.innerHTML =
        "<tr><th></th><td>No items chosen yet!</td></tr>";
    } catch (err) {
      return;
    }
    try {
      cart_template.innerHTML = "<h5>No items chosen yet!</h5>";
    } catch (err) {
      return;
    }
  } else {
    $.ajax({
      type: "POST",
      url: "/get_cart_items/",
      data: {
        products: JSON.stringify(cart)
      },
      success: function(products) {
        var data = JSON.parse(products);
        // Adjust the due total amount
        total = 0;
        data.forEach(item => {
          total += parseInt(item.fields.price);
        });
        due_amount = total;

        // Building out template
        try {
          build_cart_modal_template(data);
        } catch (err) {
          return;
        }
        try {
          build_cart_template(data);
        } catch (err) {
          return;
        }
      }
    });
    return false;
  }
};

get_cart_items();

remove_item = id => {
  for (var i = 0; i < cart.length; i++) {
    if (cart[i] == id) {
      cart.splice(i, 1);
      break;
    }
  }

  localStorage.setItem("cart_items", JSON.stringify(cart));
  items_in_cart.innerHTML = cart.length;
  get_cart_items();
};
