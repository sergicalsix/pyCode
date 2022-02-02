#https://eli5.readthedocs.io/en/latest/blackbox/permutation_importance.html
# https://qiita.com/shimopino/items/5fee7504c7acf044a521
 self.calc_permutation_importance(x, y)
        self.tmp_node_importances['l1'] = np.sort(
            self.tmp_node_importances['l1'])[::-1]
        self.tmp_node_importances['l2'] = np.sort(
            self.tmp_node_importances['l2'])[::-1]

        self.node_importances = {}
        self.node_importances['l1'] = [0] * self.hidden_size
        self.node_importances['l2'] = [0] * self.hidden_size

        # 1層目と2層目(本来なら分けるがhidden_sizeが同じなので一つにする)
        for i in range(self.hidden_size):
            # lossが一番大きいのはそれだけ重要だったということ, intのキャストはcupy配列用
            self.node_importances['l1'][int(np.argmax(
                self._loss['l1']))] = float(self.tmp_node_importances['l1'][i])
            self.node_importances['l2'][int(np.argmax(
                self._loss['l2']))] = float(self.tmp_node_importances['l2'][i])

            self._loss['l1'][int(np.argmax(self._loss['l1']))] = -1
            self._loss['l2'][int(np.argmax(self._loss['l2']))] = -1

# 隠れ層1層目
        for i in range(self.hidden_size):
            x_ = self.layers['Conv1'].forward(x)
            x_ = self.layers['Pool1'].forward(x_)
            x_ = self.layers['Conv2'].forward(x_)
            x_ = self.layers['Pool2'].forward(x_)

            x_ = self.layers['ActivateCNN1'].forward(x_)
            x_ = self.layers["Affine1"].forward(x_)
            x_ = self.layers["Activate1"].forward(x_)
            # permutation x.shape = (100,400)
            np.random.shuffle(x_[:, i])
            x_ = self.layers["Affine2"].forward(x_)
            x_ = self.layers["Activate2"].forward(x_)
            x_ = self.layers["Affine3"].forward(x_)

            x_ = self.last_layer.forward(x_)
            L = cross_entropy_error(x_, y)
            self._loss['l1'][i] = L.sum()
