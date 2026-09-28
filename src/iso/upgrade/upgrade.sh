# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

#!/bin/sh

sudo bootc switch --apply --soft-reboot=auto --transport=oci /media/cdrom/container
sudo bootc upgrade --apply --soft-reboot=auto
